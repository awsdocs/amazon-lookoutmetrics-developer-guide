# Using Amazon RDS with Lookout for Metrics<a name="services-rds"></a>

You can use Amazon Relational Database Service \(Amazon RDS\) as a datasource for an Amazon Lookout for Metrics detector\. With Amazon RDS, you can choose columns to monitor \(*measures*\) and columns that segment measure values \(dimensions\)\. The detector monitors the values in these columns to find anomalies in your data\.

The following database engines are supported:

****
+ **Amazon Aurora**
+ **MySQL**
+ **PostgreSQL**
+ **MariaDB**
+ **Microsoft SQL Server**

To use an Amazon RDS database with Lookout for Metrics, the table must have a timestamp column that is indexed for queries\. This allows Lookout for Metrics to get records for an interval without scanning the entire table\. You also need an AWS Secrets Manager secret for the detector\. The secret must have the database password and have a name that starts with `AmazonLookoutMetrics-`\.

Before you configure the dataset, you need to know the database ID, database name, table name, column names, and details about the database instance's VPC\.

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