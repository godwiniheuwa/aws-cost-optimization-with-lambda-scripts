import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Specify the instance IDs that you want to stop
    instance_ids = ['instance_id_1', 'instance_id_2']  # Add your instance IDs here
    
    # Stop the instances
    ec2.stop_instances(InstanceIds=instance_ids)
    
    return {
        'statusCode': 200,
        'body': 'Instances stopped successfully'
    }
