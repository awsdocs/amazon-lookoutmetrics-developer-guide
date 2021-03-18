# Using Amazon Redshift with Lookout for Metrics<a name="services-redshift"></a>

You can use Amazon Redshift as a datasource for an Amazon Lookout for Metrics detector\. With Amazon Redshift, you can choose columns to monitor \(*measures*\) and columns that segment measure values \(dimensions\)\. The detector monitors the values in these columns to find anomalies in your data\.

**Important**  
Lookout for Metrics can only connect to databases in a subset of Availability Zones in some Regions\. The following Availability Zones are supported\.  
**US East \(N\. Virginia\)** – `use1-az1`,`use1-az4`, `use1-az6`
**US West \(Oregon\)** – `usw2-az1`, `usw2-az2`, `usw2-az3`
**Asia Pacific \(Tokyo\)** – `apne1-az1`, `apne1-az2`, `apne1-az4`
**Other Regions** – All Availability Zones\.
Availability Zone names such as `us-west-2a` are aliases for zone IDs that vary by account\. To see which names map to which IDs in your account, visit the [EC2 dashboard](https://console.aws.amazon.com/ec2) in the AWS Management Console\.

To use an Amazon Redshift data warehouse with Lookout for Metrics, the table must have a timestamp column\. You also need an AWS Secrets Manager secret for the detector\. The secret must have the database password and have a name that starts with `AmazonLookoutMetrics-`\.

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

**To create an Amazon Redshift dataset**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Add dataset**\.

1. Choose **Amazon Redshift**\.

1. Follow the instructions to create the datasource\.

To configure metrics in Lookout for Metrics, you choose columns to be measures and dimensions\. Each measure is a column with a numerical value that you want to monitor for anomalies\. Each dimension is a column with a string value that segments the measure\(s\)\. A metric in Lookout for Metrics is a combination of a measure value and a dimension value, aggregated within an interval\. For example, *average availability in Colorado*, or *maximum temperature in furnace 17*\.

The detector reads new data from Amazon Redshift periodically, by querying records with timestamps in the most recently completed interval\. If it detects any anomalies in the metrics for the interval, it records an anomaly and sends [anomaly alerts](detectors-alerts.md), if configured\.

When you activate the detector, it uses data from several intervals to learn, before attempting to find anomalies\. For a five minute interval, the training process takes approximately one day\. Training time varies [depending on the detector's interval](gettingstarted-quotas.md#gettingstarted-quotas-coldstart)\.

**Note**  
When you add an Amazon Redshift dataset to your detector, the Lookout for Metrics console creates a [service role](permissions-service.md) with permission to use the database secret and monitor Amazon Redshift resources\. Lookout for Metrics also creates up to two [elastic network interfaces](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ElasticNetworkInterfaces.html), which allow it to connect to your VPC to access your database\. When you delete the detector, Lookout for Metrics deletes the network interfaces\.

For more information about Amazon Redshift, see [Getting started with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html) in the Amazon Redshift Getting Started\.