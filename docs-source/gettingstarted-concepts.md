# Amazon Lookout for Metrics Concepts<a name="gettingstarted-concepts"></a>

This section describes key concepts and terminology you need to understand to use Amazon Lookout for Metrics effectively\.

## Detector<a name="gettingstarted-concepts-detector"></a>

A *detector* is a Lookout for Metrics resource that monitors a dataset and identifies anomalies\. Detectors use machine learning to find patterns in data, and to distinguish between expected variations in data and legitimate anomalies\. To improve its performance, a detector learns more about your data over time\.

When you create a detector, you configure an *interval* to tell the detector how often to update the dataset and look for anomalies\. An interval can range from 5 minutes to 1 day\. At the end of each interval, the detector looks for anomalies in the data from the interval\. If all data is not available immediately at the end of each interval, you can configure an *offset* that specifies an amount of time for the detector to wait before it starts processing data\.

In addition to a dataset, a detector can have alerts\. For more information, see [ Working with detectors](lookoutmetrics-detectors.md)\.

## Datasource<a name="gettingstarted-concepts-datasource"></a>

A datasource is a service or resource that provides time\-series data for analysis\. A datasource has dated records that each have metrics and \(optionally\) dimensions\. If you make an application that writes records to Amazon S3 as they occur, you can use the Amazon S3 bucket as a datasource\.

Lookout for Metrics integrates with other AWS services to provide additional datasources\. A detector can access records in a relational database in Amazon Relational Database Service or Amazon Redshift, metrics in Amazon CloudWatch, or data in an Amazon AppFlow flow\. With these services, you can collect data from even more services and resources\.

## Dataset<a name="gettingstarted-concepts-dataset"></a>

A *dataset* is a detector's copy of your data\. At the end of each interval, the detector copies metrics and dimensions from a datasource into its dataset for analysis\. Each row or document in a dataset is called a *record*\. Each labeled value or key\-value pair in a record is a *field*\. Each record much have a timestamp field and at least one field that the detector monitors, called a *measure*\.

A dataset can have continuous data, historical data or both\. A detector looks for anomalies in continuous data, and uses historical data for learning\. If its dataset has only historical data, a detector runs in *backtest mode*\. In backtest mode, a detector uses most of the data for learning and attempts to find anomalies in a smaller subset of recent data\.

Datasets have a datasource, a service role, and a mapping that tells the detector which values to monitor\. For more information, see [Managing a dataset in Amazon S3](detectors-dataset.md)\.

## Metrics<a name="gettingstarted-concepts-metrics"></a>

After giving your detector a datasource, you choose fields to be the dataset's measures\. *Measures* are the primary fields that the detector monitors\. You can also configure up to five additional fields as *dimensions*\. Dimensions are secondary fields that create subgroups of measures based on their value\. Each combination of metric and dimension is called a *metric*\.

For example, you can choose a field named `availability` for a measure\. If you don't choose a dimension, the detector monitors availability across all records\. If you choose a field named `country` for a dimension, then the detector monitors availability in each country as a separate metric: *availability in Canada*, *availability in Italy*, and so on\.

For more information, see [Setting up a detector](detectors-setup.md)\.

## Alert<a name="gettingstarted-concepts-alert"></a>

To send a notifications or initiate a processing workflow when the detector finds an anomaly, you can create an alert\. An alert has a target that can be an Amazon Simple Notification Service \(Amazon SNS\) topic or an AWS Lambda function\. When the detector finds an anomaly with a severity score over a configurable threshold, the alert sends a record of the anomaly to the target\. A severity score is a number between 0 and 100 that indicates how far the metric value is outside of the expected range\.

You can process the anomaly record in the programming language of your choice with a Lambda function\. With an Amazon SNS topic, you can send the anomaly record to multiple subscribers\. A subscriber can use any protocol that Amazon SNS supports, including email addresses, mobile devices, and webhooks\. With a webhook, you can send the anomaly record to third\-party services, such as Slack\.

For more information, see [Creating alerts ](detectors-alerts.md)\.

## Feedback<a name="gettingstarted-concepts-feedback"></a>

When the detector finds an anomaly, it creates a report with details about all of the metrics that had unexpected values during the interval in the Lookout for Metrics console\. When you view this report , you can provide feedback on the relevance of each metric\. The detector uses your feedback to improve its accuracy\.

For more information, see [Viewing anomalies ](detectors-anomalies.md)\.