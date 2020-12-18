# Service roles for Amazon Lookout for Metrics<a name="permissions-service"></a>

You can use service roles to grant Amazon Lookout for Metrics permission to access data and send alerts to other services\. A service role is an AWS Identity and Access Management \(IAM\) role that an AWS service can use to access resources from other services in your account\. For example, to invoke an AWS Lambda function when an alert is sent, Lookout for Metrics assumes a role that allows it to invoke the function\. Lookout for Metrics uses a separate service role for each supported data source and notification target, including Amazon Simple Storage Service \(Amazon S3\), Lambda, and Amazon Simple Notification Service \(Amazon SNS\)

When you configure a dataset or alert in the Lookout for Metrics console, the console can create the required role for you if you have the necessary permissions\. If you don't have permissions to create roles, or if you use the Lookout for Metrics API to manage resources, you can [create the roles manually](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html)\. Service roles must have the following trust policy\.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lookoutmetrics.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

The trust policy allows Lookout for Metrics to assume the role\.