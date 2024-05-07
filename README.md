# aws-cost-optimization-with-lambda-scripts

# Auto-Scaling Optimization Lambda Function

This repository contains a Python script for an AWS Lambda function designed to optimize auto-scaling settings based on workload.

## Purpose

The purpose of this Lambda function is to monitor the workload on AWS services such as EC2, ECS, and RDS, and dynamically adjust the auto-scaling settings to optimize resource utilization and cost. Specifically, it monitors CPU utilization of EC2 instances and adjusts the desired capacity of the Auto Scaling group accordingly.

## Features

- Monitors CPU utilization of EC2 instances using CloudWatch metrics.
- Calculates average CPU utilization across all instances.
- Adjusts auto-scaling settings based on average CPU utilization:
  - Increases desired capacity if CPU utilization exceeds 80%.
  - Decreases desired capacity if CPU utilization falls below 20%.

## Prerequisites

Before using this Lambda function, ensure you have:

- An AWS account with permissions to create and manage Lambda functions, CloudWatch Events, EC2 instances, and Auto Scaling groups.
- AWS CLI configured with appropriate credentials.

## Usage

1. Clone or download this repository to your local machine.
2. Update the Python script (`auto_scaling_optimization.py`) with your Auto Scaling group name and any customization required for your use case.
3. Deploy the Python script as an AWS Lambda function.
4. Create a CloudWatch Event Rule to trigger the Lambda function at a scheduled interval (e.g., every 5 minutes).
5. Monitor the CloudWatch logs and Auto Scaling group metrics to verify the behavior of the Lambda function.

## Configuration

You may need to customize the following parameters in the Python script:

- `adjust_auto_scaling_capacity()`: Update the Auto Scaling group name to match your environment.
- Thresholds for increasing and decreasing desired capacity based on CPU utilization.


# Scheduled Instance Start/Stop with AWS Lambda and CloudWatch Events

Automating the start and stop of EC2 instances based on a schedule can help reduce costs by running instances only when needed. This guide outlines the steps to create Lambda functions triggered by CloudWatch Events to achieve scheduled instance start/stop.

## Prerequisites

Before you begin, ensure you have:

- An AWS account with permissions to create Lambda functions, CloudWatch Events rules, and EC2 instances.
- Basic knowledge of AWS Lambda, CloudWatch Events, and EC2.

## Steps

### 1. Create IAM Role for Lambda Function

Create an IAM role that grants necessary permissions to your Lambda function to start and stop EC2 instances. This role should include permissions like `ec2:StartInstances` and `ec2:StopInstances`.

### 2. Write Lambda Functions

Write two Lambda functions: one to start EC2 instances and another to stop them. Below are sample Python code snippets for each function:

#### Lambda Function to Start Instances:

```python
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instance_ids = ['instance_id_1', 'instance_id_2']  # Add your instance IDs here
    ec2.start_instances(InstanceIds=instance_ids)
    return {
        'statusCode': 200,
        'body': 'Instances started successfully'
    }


# AWS Lambda Function: Unused Resource Cleanup

This AWS Lambda function is designed to automatically clean up unused resources in your AWS environment. It scans for unattached EBS volumes and orphaned snapshots, and deletes them if they have been unused for more than 7 days.

## Overview

The Lambda function is triggered by an event and uses the Boto3 library to interact with the AWS resources. It performs the following tasks:

- **Scan for Unattached EBS Volumes**: It describes the volumes and identifies those with a status of "available", indicating that they are unattached.
- **Delete Unattached EBS Volumes**: It deletes unattached EBS volumes that have been unused for more than 7 days.
- **Scan for Orphaned Snapshots**: It describes the snapshots and identifies those that do not belong to any EBS volume.
- **Delete Orphaned Snapshots**: It deletes orphaned snapshots that have been unused for more than 7 days.

## Prerequisites

Before using this Lambda function, ensure you have:

- An AWS account with appropriate permissions to create and execute Lambda functions, as well as manage EC2 resources.
- Basic knowledge of AWS Lambda, Boto3 library, and EC2 resources.

## Setup

1. **Create Lambda Function**: Use the provided code to create a new Lambda function in your AWS account.
2. **Configure Trigger**: Set up a CloudWatch Event rule to trigger the Lambda function at a desired schedule (e.g., daily).
3. **IAM Permissions**: Ensure the Lambda function's execution role has the necessary permissions to describe and delete EC2 resources.

## Notes

- Adjust the age threshold (currently set to 7 days) in the Lambda function code to suit your requirements.
- Exercise caution when deleting resources automatically. Make sure the Lambda function is thoroughly tested in a non-production environment before deploying to production.
- Monitor the execution of the Lambda function and review the CloudWatch logs to ensure it behaves as expected.


## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

