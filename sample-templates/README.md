# Sample templates

Use the CloudFormation templates in this folder to create resources for use with Amazon Lookout for Metrics. You can modify the parameters in a template to change or restrict the resources that they allow access to.

**Templates**
- `servicerole-s3` - An IAM role that gives Lookout for Metrics permission to access S3 buckets, SNS topics, and Lambda functions that have names prefixed with `lookoutmetrics-`.
- `servicerole-rds` - An IAM role that gives Lookout for Metrics permission to use secrets prefixed with `AmazonLookout` to get database credentials, monitor Amazon RDS DB instances, and create network interfaces. Includes permission to send anomaly alerts to SNS topics and Lambda functions that have names prefixed with `lookoutmetrics-`.
- `vpc-network` - A virtual private cloud (VPC) with two private subnets, a public subnet, and a VPC endpoint that allows API calls to Lookout for Metrics without internet acccess.

To create a stack, use the `1-create-stack.sh` script with the name of the template as an argument.

        $ ./1-create-stack.sh servicerole-s3
        Creating stack lookoutmetrics-servicerole-s3
        Waiting for changeset to be created..
        Waiting for stack create/update to complete
        Successfully created/updated stack - lookoutmetrics-servicerole-s3

To delete a stack, use the `2-delete-stack.sh` script.

        $ ./2-delete-stack.sh servicerole-s3
        Delete stack lookoutmetrics-servicerole-s3? (y/n)y
