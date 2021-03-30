# Pricing<a name="gettingstarted-pricing"></a>

Pricing for Amazon Lookout for Metrics is based on the number of metrics that your detector monitors for anomalies\. This number varies based on the number of measures and dimensions that you choose when you configure a dataset\. It can also vary from interval to interval, based on the number of different values that appear for each dimension\.

For example, if you choose a field named `availability` as a measure and choose no dimensions, Lookout for Metrics monitors values of `availability` for each interval \(1 metric\)\. If you choose `availability` as a measure and `state` as a dimension, where `state` has 50 possible values, Lookout for Metrics monitors values of `availability` for each value of `state` \(50 metrics\)\.

For another example, if you choose a field named `orders` with a dimension of `state`, the number of metrics can vary from interval to interval\. You might have orders from 40 states in 1 interval, and 45 in another\. For these intervals, the number of metrics would be 40 and 45, respectively\.

For specific prices and pricing examples, see [Amazon Lookout for Metrics pricing ](https://aws.amazon.com/lookout-for-metrics/pricing/)\.

**Topics**
+ [Charges for metrics](#gettingstarted-pricing-metrics)
+ [Charges for other services](#gettingstarted-pricing-otherservices)

## Charges for metrics<a name="gettingstarted-pricing-metrics"></a>

When a detector monitors data, it generates charges for each metric that appears in the dataset during an interval\. To determine the number of metrics, the number of measures that you assign when you configure your dataset is multiplied by the number of unique combinations of dimension name and dimension value that appear in live data\.

For example, if you choose 2 fields for measures, and 3 dimensions that each have 5 possible values, the maximum number of metrics that can appear in an interval is 30\. If not all dimension values appear in every interval, the number of metrics can vary between 6 and 30 for each interval\.

**Important**  
The cost of using a detector increases linearly with the number of different values that appear in each interval for the dimensions that you configure for your dataset\. For example, if you use a dimension named `continent` that has 7 possible values, the cost of that dimension is limited by the number of measures times 7\. If you use a dimension named `id` that stores a GUID, the cost of the dimension increases scales with the number of GUIDs that appear in the data\.

## Charges for other services<a name="gettingstarted-pricing-otherservices"></a>

When Lookout for Metrics copies data into a dataset from a datasource, data transfer and API usage charges can apply\. Several services have a [free tier](https://aws.amazon.com/free/) that applies if your overall use of that service is low\. Some free tiers are limited to the first year after you create your account\. Others apply permanently or under specific conditions\. When using Lookout for Metrics, you might incur charges for the following services: 

****
+ [Amazon Simple Storage Service \(Amazon S3\)](https://aws.amazon.com/s3/pricing/) – Charges for storage, API requests, and data transfer\. Eligible for free tier under certain conditions\.
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/pricing/) – Charges for CloudWatch metric storage and retrieval \(transfer out\)\. Eligible for free tier under certain conditions\.
+ [Amazon Relational Database Service](https://aws.amazon.com/rds/pricing/) – Charges for database instances and data transfer\. Eligible for free tier under certain conditions\.
+ [Amazon Redshift](https://aws.amazon.com/redshift/pricing/) – Charges for data warehouse nodes and data transfer\. Eligible for free tier under certain conditions\.
+ [Amazon AppFlow](https://aws.amazon.com/appflow/pricing/) – Charges per flow run \(transfer in\) and for each GB of data processed\.

This list highlights the main billing components of each service\. Additional charges apply for use of optional features\. For more information, see the pricing page for each service\.