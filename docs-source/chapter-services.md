# Using Amazon Lookout for Metrics with other services<a name="chapter-services"></a>

Amazon Lookout for Metrics works with other AWS services to provide additional options for datasources and notification targets\. In addition to reading metrics data from an Amazon Simple Storage Service \(Amazon S3\) bucket, you can create datasets from databases, observability services, and cloud applications\. When a detector finds anomalies, it can invoke a Lambda function or send anomaly alerts to an Amazon SNS topic\.

To use a cloud application such as Salesforce as a datasource, you use Amazon AppFlow\. Amazon AppFlow is an AWS service that supports additional datasources by providing a *flow* that third party services can write to\.

Lookout for Metrics integrates with other services to provide additional datasources and alert channels\. Lookout for Metrics supports the following services as datasources\.

****
+ [Amazon S3](services-s3.md) – Read metrics data from text objects in a bucket\. Supports using historical data for training and testing a detector\.
+ [Amazon CloudWatch](services-cloudwatch.md) – Analyze CloudWatch metrics sent by an AWS service, AWS resource, or an application\.
+ [Amazon Relational Database Service \(Amazon RDS\)](services-rds.md) – Analyze items in a relational database\. The following database engines are supported:

****
  + **Amazon Aurora**
  + **MySQL**
  + **PostgreSQL**
  + **MariaDB**
  + **Microsoft SQL Server**
+ [Amazon Redshift](services-redshift.md) – Analyze items in a Amazon Redshift data warehouse\.
+ [Amazon AppFlow](services-appflow.md) – Analyze data flow from a web service with an Amazon AppFlow data flow\. The following services are supported:
  + **Salesforce**
  + **Marketo**
  + **Dynatrace**
  + **Singular**
  + **Zendesk**
  + **Servicenow**
  + **Infor Nexus**
  + **Trendmicro**
  + **Veeva**
  + **Google Analytics**
  + **Amplitude**

You can configure a detector to send notifications to the following services and resources\.

****
+ **AWS Lambda** – Invoke a Lambda function with an event that contains details about an anomaly\.
+ **Amazon Simple Notification Service \(Amazon SNS\)** – Send a notification to a topic that email, SMS, or web application subscribers\. Lookout for Metrics supports the following application channels with Amazon SNS:

****
  + **PagerDuty**
  + **Slack**
  + **Datadog**

To interact with other AWS services, Lookout for Metrics uses permissions from an AWS Identity and Access Management \(IAM\) service role\. A service role is an IAM role that you create to give a service permission to access AWS resources in your account\. For more information, see [Amazon Lookout for Metrics permissions](lookoutmetrics-permissions.md)\.

**Topics**
+ [Using Amazon AppFlow with Lookout for Metrics](services-appflow.md)
+ [Using Amazon CloudWatch with Lookout for Metrics](services-cloudwatch.md)
+ [Using AWS Lambda with Lookout for Metrics](services-lambda.md)
+ [Using Amazon RDS with Lookout for Metrics](services-rds.md)
+ [Using Amazon Redshift with Lookout for Metrics](services-redshift.md)
+ [Using Amazon SNS with Lookout for Metrics](services-sns.md)
+ [Using Amazon S3 with Lookout for Metrics](services-s3.md)