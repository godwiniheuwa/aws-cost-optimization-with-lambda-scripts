import boto3
from datetime import datetime, timedelta

def get_cpu_utilization(instance_id):
    """
    Retrieve CPU utilization metric for a specific EC2 instance using CloudWatch.
    
    Parameters:
    instance_id (str): The ID of the EC2 instance.
    
    Returns:
    float: Average CPU utilization percentage over the last 5 minutes.
    """
    cloudwatch = boto3.client('cloudwatch')
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instance_id
            },
        ],
        StartTime=(datetime.now() - timedelta(minutes=5)).isoformat(),
        EndTime=datetime.now().isoformat(),
        Period=300,
        Statistics=['Average'],
        Unit='Percent'
    )
    if 'Datapoints' in response and len(response['Datapoints']) > 0:
        return response['Datapoints'][0]['Average']
    else:
        return None

def adjust_auto_scaling_capacity(group_name, desired_capacity):
    """
    Adjust the desired capacity of an Auto Scaling group.
    
    Parameters:
    group_name (str): The name of the Auto Scaling group.
    desired_capacity (int): The desired capacity to set for the Auto Scaling group.
    """
    autoscaling = boto3.client('autoscaling')
    response = autoscaling.update_auto_scaling_group(
        AutoScalingGroupName=group_name,
        DesiredCapacity=desired_capacity
    )
    print(f"Auto Scaling Group '{group_name}' desired capacity set to {desired_capacity}")

def lambda_handler(event, context):
    """
    Lambda function handler.
    
    Parameters:
    event (dict): The event data passed to the Lambda function.
    context (LambdaContext): The runtime information of the Lambda function.
    """
    ec2 = boto3.client('ec2')
    
    # Get a list of EC2 instances in your Auto Scaling group
    response = ec2.describe_instances()
    total_cpu_utilization = 0
    total_instances = 0
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            cpu_utilization = get_cpu_utilization(instance_id)
            if cpu_utilization is not None:
                total_cpu_utilization += cpu_utilization
                total_instances += 1

    if total_instances > 0:
        # Calculate average CPU utilization across all instances
        average_cpu_utilization = total_cpu_utilization / total_instances
        print(f"Average CPU Utilization: {average_cpu_utilization}%")
        
        # Adjust auto-scaling settings based on average CPU utilization
        if average_cpu_utilization > 80:
            adjust_auto_scaling_capacity('my-auto-scaling-group', 2 * total_instances)
        elif average_cpu_utilization < 20:
            adjust_auto_scaling_capacity('my-auto-scaling-group', total_instances // 2)
