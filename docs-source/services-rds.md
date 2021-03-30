# Using Amazon RDS with Lookout for Metrics<a name="services-rds"></a>

You can use Amazon Relational Database Service \(Amazon RDS\) as a datasource for an Amazon Lookout for Metrics detector\. With Amazon RDS, you can choose columns to monitor \(*measures*\) and columns that segment measure values \(dimensions\)\. The detector monitors the values in these columns to find anomalies in your data\.

**Important**  
Lookout for Metrics can only connect to databases in a subset of Availability Zones in some Regions\. The following Availability Zones are supported\.  
**US East \(N\. Virginia\)** – `use1-az1`,`use1-az4`, `use1-az6`
**US West \(Oregon\)** – `usw2-az1`, `usw2-az2`, `usw2-az3`
**Asia Pacific \(Tokyo\)** – `apne1-az1`, `apne1-az2`, `apne1-az4`
**Other Regions** – All Availability Zones\.
Availability Zone names such as `us-west-2a` are aliases for zone IDs that vary by account\. To see which names map to which IDs in your account, visit the [EC2 dashboard](https://console.aws.amazon.com/ec2) in the AWS Management Console\.

The following database engines are supported:

****
+ **Amazon Aurora**
+ **MySQL**
+ **PostgreSQL**
+ **MariaDB**
+ **Microsoft SQL Server**

To use an Amazon RDS database with Lookout for Metrics, the table must have a timestamp column that is indexed for queries\. This allows Lookout for Metrics to get records for an interval without scanning the entire table\. You also need an AWS Secrets Manager secret for the detector\. The secret must have the database password and have a name that starts with `AmazonLookoutMetrics-`\.

Before you configure the dataset, you need to know the following information\.

****
+ **DB identifier** – The unique identifier of the DB instance or cluster\. For example, `mysql-dbi` or `ld1xmplvzghgn47`\.
+ **Database name** – The software\-level database name\. For example, `mydb`\.
+ **Table name** – The name of the table\. For example, `events`\.
+ **Column names** – The names of columns that contain timestamps, measures, and dimensions\.
+ **Subnets** – The virtual private cloud \(VPC\) subnets where the detector creates network interfaces to connect to the database\. For example, `subnet-0752xmpl92bf2e4b7`\.
+ **Security group** – A VPC security group that allows traffic to the database\. For example, `sg-0f92xmplfbad0bc95`\.
+ **Secret name** – The name of an AWS Secrets Manager secret that the detector uses to retrieve the database password\. For example, `AmazonLookoutMetrics-mysqldbi`\.
+ **Secret ID** – The ID of the secret, for generating a service role that can access it\. For example, `AmazonLookoutMetrics-mysqldbi-Nxmplo`\.

**To create an Amazon RDS dataset**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Add dataset**\.

1. Choose one of the available database engines:

****
   + **Amazon Aurora**
   + **MySQL**
   + **PostgreSQL**
   + **MariaDB**
   + **Microsoft SQL Server**

1. Follow the instructions to create the datasource\.

To configure metrics in Lookout for Metrics, you choose columns to be measures and dimensions\. Each measure is a column with a numerical value that you want to monitor for anomalies\. Each dimension is a column with a string value that segments the measure\(s\)\. A metric in Lookout for Metrics is a combination of a measure value and a dimension value, aggregated within an interval\. For example, *average availability in Colorado*, or *maximum temperature in furnace 17*\.

The detector reads new data from Amazon RDS periodically, by querying records with timestamps in the most recently completed interval\. If it detects any anomalies in the metrics for the interval, it records an anomaly and sends [anomaly alerts](detectors-alerts.md), if configured\.

When you activate the detector, it uses data from several intervals to learn, before attempting to find anomalies\. For a five minute interval, the training process takes approximately one day\. Training time varies [depending on the detector's interval](gettingstarted-quotas.md#gettingstarted-quotas-coldstart)\.

**Note**  
When you add an Amazon RDS dataset to your detector, the Lookout for Metrics console creates a [service role](permissions-service.md) with permission to use the database secret and monitor Amazon RDS resources\. Lookout for Metrics also creates up to two [elastic network interfaces](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ElasticNetworkInterfaces.html), which allow it to connect to your VPC to access your database\. When you delete the detector, Lookout for Metrics deletes the network interfaces\.

For more information about Amazon RDS, see [Getting started with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html) in the Amazon RDS User Guide\.

**Topics**
+ [Sample IAM policies](#services-rds-samplepolicies)
+ [Sample AWS CloudFormation templates](#services-rds-sampletemplates)

## Sample IAM policies<a name="services-rds-samplepolicies"></a>

The GitHub repository for this guide provides [sample IAM policies](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-policies) that you can use as reference for developing service roles\. You can use a single role that grants permission for both importing data and sending alerts by combining the applicable policies\.

**Example [datasource\-rds\.json](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-policies/datasource-rds.json) – Monitor and access an Amazon RDS DB instance**  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "rds:DescribeDBInstances"
            ],
            "Resource": [
                "arn:aws:rds:${Region}:${Account}:db:${DatabaseId}"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "rds:DescribeDBSubnetGroups"
            ],
            "Resource": "arn:aws:rds:${Region}:${Account}:subgrp:*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "arn:aws:secretsmanager:${Region}:${Account}:secret:${SecretId}"
            ],
            "Effect": "Allow",
            "Condition": {
                "ForAllValues:StringEquals": {
                    "secretsmanager:VersionStage": "AWSCURRENT"
                }
            }
        },
        ...
```

The second sample policy shows how to grant the detector permission to connect to a database across accounts\. The account with the database instance \(Account B\) must be in the same organization and share its subnet with the account that contains the detector \(`AccountA`\)\.

**Example [datasource\-rds\-xaccount\.json](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-policies/datasource-rds-xaccount.json) – Cross\-account access**  

```
        ...
        {
            "Action": [
                "ec2:CreateNetworkInterface"
            ],
            "Resource": [
                "arn:aws:ec2:${Region}:${AccountA}:network-interface/*",
                "arn:aws:ec2:${Region}:${AccountA}:security-group/*",
                "arn:aws:ec2:${Region}:${AccountB}:subnet/${SubnetId}"
            ],
            "Effect": "Allow"
        },
        ...
```

For more information, see [Working with shared VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html) in the *Amazon VPC User Guide*\.

## Sample AWS CloudFormation templates<a name="services-rds-sampletemplates"></a>

The GitHub repository for this guide provides sample AWS CloudFormation templates that you can use to automate the creation of service roles\. The templates use parameters and naming patterns to apply least\-privilege permissions where possible\.

The sample template creates a service role that gives Lookout for Metrics permission to use secrets prefixed with `AmazonLookout` to get database credentials, monitor Amazon RDS DB instances, and create network interfaces\.

**Example [servicerole\-rds\.yml](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-templates/servicerole-rds.yml) – Amazon S3 and Lambda permissions**  

```
Resources:
  serviceRole:
    Type: AWS::IAM::Role
    Properties:
      Policies:
        - PolicyName: rds-access
          PolicyDocument:
            Version: 2012-10-17
            Statement:
            - Action:
              - rds:DescribeDBInstances
              Resource:
              - !Sub arn:${AWS::Partition}:rds:${AWS::Region}:${AWS::AccountId}:db:${databaseId}
              Effect: Allow
            - Action:
              - rds:DescribeDBSubnetGroups
              Resource: !Sub arn:${AWS::Partition}:rds:${AWS::Region}:${AWS::AccountId}:subgrp:*
              Effect: Allow
            - Action:
              - secretsmanager:GetSecretValue
              Resource:
              - !Sub arn:${AWS::Partition}:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:${secretId}
              Effect: Allow
              Condition:
                ForAllValues:StringEquals:
                  secretsmanager:VersionStage: AWSCURRENT
```

For more information, see [Sample templates](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-templates) in the GitHub repo\.