# Working with detectors<a name="lookoutmetrics-detectors"></a>

In Amazon Lookout for Metrics, a *detector* is a resource that monitors a dataset and identifies *anomalies* \(data that falls outside of the expected range\)\. Detectors use machine learning \(ML\) to find patterns in business data, and to distinguish between expected variations in data and legitimate anomalies\. A detector can monitor a dataset that contains metrics data that you manage in Amazon Simple Storage Service \(Amazon S3\), live data from another service such as Amazon CloudWatch, or events from a database\. When new data points fall outside of the expected range, the detector records the anomaly and sends an alert\.

A [dataset](detectors-dataset.md) is a collection of timestamped data points that can each have multiple metrics\. You choose one of the metrics to be the *measure*, which is the primary metric that the detector monitors for anomalies\. You can also configure up to five additional metrics as *dimensions*\. Dimensions are secondary metrics that the detector uses to segment anomalies and identify contributing factors\.

Detectors primarily work against live data\. For an Amazon Simple Storage Service \(Amazon S3\) datasource, you populate a bucket with data in real time as it is generated\. For other datasources, the detector reads data directly from the other service\. 

When you create a detector, you can also provide *historical data*\. Lookout for Metrics uses historical data to train the detector to identify anomalies more accurately\.

When you create a detector, you choose how often it analyzes data\. The *interval* can be between 5 minutes and 1 day\. To allow time for the datasource to collect all data before analysis starts, you also configure a *delay* on the dataset\. At the end of an interval, the detector waits for the duration of the delay before analyzing data\.

Every time it runs, the detector analyzes all of the data generated during the interval, identifies anomalous data points, and assigns a severity score to each\. If the severity of an anomaly exceeds a *threshold*, the detector sends an *alert*\. You can [configure alert targets](detectors-alerts.md) to send a notification to an Amazon Simple Notification Service \(Amazon SNS\) topic, or to invoke an AWS Lambda function for processing\. If you get too many or too few results, you can change the threshold that triggers the alert\.

**Topics**
+ [Setting up a detector](detectors-setup.md)
+ [Managing detectors](detectors-manage.md)
+ [Managing a dataset in Amazon S3](detectors-dataset.md)
+ [Viewing anomalies](detectors-anomalies.md)
+ [Creating alerts](detectors-alerts.md)