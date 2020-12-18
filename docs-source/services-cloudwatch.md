# Using Amazon CloudWatch with Lookout for Metrics<a name="services-cloudwatch"></a>

You can use Amazon CloudWatch metricsas a datasource for an Amazon Lookout for Metrics detector\. Most AWS services send metrics to CloudWatch automatically when you use them\. You can create a dataset from these metrics, or from metrics that you send to CloudWatch\. You can send metrics to CloudWatch from your application code, or from software such as [StatsD](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-custom-metrics-statsd.html) or [collectd](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-custom-metrics-collectd.html)\.

In CloudWatch, a metric can have a name and value, and optionally can also have a dimension name and dimension value\. For example, Amazon EC2 has a metric named `CPUUtilization` with a value that is a number between 0 and 100, and a dimension named `InstanceId` that has the unique ID of an instance\.

**To create a CloudWatch dataset**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Add dataset**\.

1. For **Datasource**, choose **CloudWatch**\.

1. Follow the instructions to create the datasource\.

To configure metrics in Lookout for Metrics, you choose a CloudWatch namespace and dimension first, and then choose one or more CloudWatch metrics to be measures for the dataset\. For CloudWatch metrics that apply to all resouces in an AWS Region, or otherwise don't have a dimension in CloudWatch, you set **Dimensions** to **None**\.

For example, in AWS Lambda you can monitor concurrency by function, by resource \(function version or alias\), or across all functions in a Region\. If you choose `ConcurrentExecutions` as a measure and `Function Name` as a dimension, then the detector monitors *concurrency for function\-a* and *concurrency for function\-b* as two Lookout for Metrics metrics\.

The detector reads new data from CloudWatch periodically, by reading the values of metrics that occur in each interval\. It aggregates the values of each metric for the interval and looks for anomalies\. It records anomalies and sends [anomaly alerts](detectors-alerts.md), if configured\.

When you activate the detector, it uses data from several intervals to learn, before attempting to find anomalies\. For a five minute interval, the training process takes approximately one day\. Training time varies [depending on the detector's interval](gettingstarted-quotas.md#gettingstarted-quotas-coldstart)\.

When you add a CloudWatch dataset to your detector, the Lookout for Metrics console creates a [service role](permissions-service.md) with permission to read metrics\.