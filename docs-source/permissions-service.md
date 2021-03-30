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

**Topics**
+ [Sample IAM policies](#permissions-service-samplepolicies)
+ [Sample AWS CloudFormation templates](#permissions-service-sampletemplates)

## Sample IAM policies<a name="permissions-service-samplepolicies"></a>

The GitHub repository for this guide provides sample IAM policies that you can use as reference for developing service roles\. You can use a single role that grants permission for both importing data and sending alerts by combining the applicable policies\.

**Example [alert\-lambda\.json](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-policies/alert-lambda.json) – Send anomaly alerts to a Lambda function**  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Resource": [
                "arn:aws:lambda:${Region}:${Account}:function:${FunctionName}"
            ]
        }
    ]
}
```

Values contained in brackets are placeholders for account\-specific information such as resource names and account IDs\. For more information, see [Sample policies](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-policies) in the GitHub repo\.

## Sample AWS CloudFormation templates<a name="permissions-service-sampletemplates"></a>

The GitHub repository for this guide provides sample AWS CloudFormation templates that you can use to automate the creation of service roles\. The templates use parameters and naming patterns to apply least\-privilege permissions where possible\.

The following sample template creates a service role that gives Lookout for Metrics permission to access S3 buckets, SNS topics, and Lambda functions that have names prefixed with `lookoutmetrics-`\.

**Example [servicerole\-s3\.yml](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-templates/servicerole-s3.yml) – Amazon S3 and Lambda permissions**  

```
Parameters:
  bucketName:
    Description: Bucket name
    Type: String
    Default: lookoutmetrics-*
  queueName:
    Description: Queue name
    Type: String
    Default: lookoutmetrics-*
  functionName:
    Description: Function name
    Type: String
    Default: lookoutmetrics-*
Resources:
  serviceRole:
    Type: AWS::IAM::Role
    Properties:
      Policies:
        - PolicyName: read-s3
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action: 
                  - s3:ListBucket
                  - s3:GetBucketAcl
                Resource: !Sub arn:${AWS::Partition}:s3:::${bucketName}
              - Effect: Allow
                Action:
                  - s3:GetObject
                  - s3:GetBucketAcl
                Resource: !Sub arn:aws:s3:::${bucketName}/*
        - PolicyName: invoke-function
          PolicyDocument:
            Version: 2012-10-17
            Statement:
            - Effect: Allow
              Action: lambda:InvokeFunction
              Resource: !Sub arn:${AWS::Partition}:lambda:${AWS::Region}:${AWS::AccountId}:${functionName}
...
```

For more information, see [Sample templates](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-templates) in the GitHub repo\.