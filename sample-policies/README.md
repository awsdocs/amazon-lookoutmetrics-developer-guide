# Sample policies

Use the policies in this folder as reference for creating a service role for a detector. You can use a single role that grants permission for both importing data and sending alerts by combining the applicable policies.

**Policies**
- `alert-lambda.json` - Permission to send anomaly alerts to an AWS Lambda function.
- `alert-sns.json` - Permission to send anomaly alerts to an Amazon SNS topic.
- `datasource-appflow.json` - Permission to import data from an Amazon AppFlow flow.
- `datasource-cloudwatch.json` - Permission to import data from Amazon CloudWatch.
- `datasource-rds.json` - Permission to import data from an Amazon RDS database.
- `datasource-rds-xaccount.json` - Permission to import data from an Amazon RDS database in a shared VPC subnet in a second account.
- `datasource-redshift.json` - Permission to import data from an Amazon Redshift data warehouse.
- `datasource-redshift-xaccount.json` - Permission to import data from an Amazon Redshift data warehouse in a shared VPC subnet in a second account.
- `datasource-s3.json` - Permission to import data from an Amazon S3 bucket.

The sample policies include placeholders for account-specific information such as `${Account}` and `${Region}`. For sample CloudFormation templates that automate the creation of roles with the correct information, see the [sample-templates](/sample-templates) folder.