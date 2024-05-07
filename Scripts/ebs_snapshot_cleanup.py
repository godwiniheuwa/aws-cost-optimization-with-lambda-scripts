import boto3
import datetime

def lambda_handler(event, context):
    # Initialize Boto3 clients
    ec2 = boto3.client('ec2')
    
    # Get current time
    current_time = datetime.datetime.utcnow()
    
    # Describe unattached EBS volumes
    response_volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    unattached_volumes = [volume for volume in response_volumes['Volumes']]
    
    # Delete unattached EBS volumes older than 7 days
    for volume in unattached_volumes:
        volume_id = volume['VolumeId']
        
        # Get last attachment time, if available
        last_attachment_time = None
        if volume['Attachments']:
            last_attachment_time = volume['Attachments'][0]['AttachTime']
        
        # Calculate age since last attachment or creation time
        if last_attachment_time:
            age = current_time - last_attachment_time
        else:
            volume_creation_time = volume['CreateTime']
            age = current_time - volume_creation_time
        
        # If volume is older than 7 days, delete it
        if age.days > 7:
            ec2.delete_volume(VolumeId=volume_id)
    
    # Describe snapshots
    response_snapshots = ec2.describe_snapshots(OwnerIds=['self'])
    all_snapshots = response_snapshots['Snapshots']
    
    # Find snapshots not belonging to an EBS volume
    orphan_snapshots = []
    for snapshot in all_snapshots:
        if 'VolumeId' not in snapshot:
            snapshot_id = snapshot['SnapshotId']
            snapshot_creation_time = snapshot['StartTime']
            age = current_time - snapshot_creation_time
            
            # If snapshot is older than 7 days, delete it
            if age.days > 7:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
    
    return {
        'statusCode': 200,
        'body': 'Unused EBS volumes and snapshots deleted successfully'
    }
