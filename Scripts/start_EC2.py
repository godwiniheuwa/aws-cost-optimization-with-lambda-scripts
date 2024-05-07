import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Specify the instance IDs that you want to start
    instance_ids = ['instance_id_1', 'instance_id_2']  # Add your instance IDs here
    
    # Start the instances
    ec2.start_instances(InstanceIds=instance_ids)
    
    return {
        'statusCode': 200,
        'body': 'Instances started successfully'
    }
