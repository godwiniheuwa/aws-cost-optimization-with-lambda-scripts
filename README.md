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

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

