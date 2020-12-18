# Amazon Lookout for Metrics Concepts<a name="gettingstarted-concepts"></a>

With Amazon Lookout for Metrics, you run a detector to monitor data and find anomalies\. A detector has a dataset that contains data from a datasource such as an Amazon Simple Storage Service \(Amazon S3\) bucket or a relational database\. To receive notifications or initiate processing workflows when an anomaly occurs, you can add alerts to the detector\.

## Detector<a name="gettingstarted-concepts-detector"></a>

A *detector* is an Lookout for Metrics resource that monitors a dataset and identifies anomalies\. Detectors use machine learning to find patterns in data, and to distinguish between expected variations in data and legitimate anomalies\. To improve its performance, a detector learns more about your data over time\.

When you create a detector, you configure an *interval* to tell the detector how often to update the dataset and look for anomalies\. An interval can range from 5 minutes to 1 day\. At the end of each interval, the detector aggregates the latest data and looks for unexpected values\.

In addition to a dataset, a detector can have alarms\. For more information, see [ Working with detectors](lookoutmetrics-detectors.md)\.

## Dataset<a name="gettingstarted-concepts-dataset"></a>

A *dataset* is a detector's copy of your data\. At the end of each interval, the detector copies data from a datasource into its dataset for analysis\. A dataset can import data from an Amazon S3 bucket that you update periodically, from a relational database, or from an AWS service that collects data, such as Amazon CloudWatch\.

Data can be stored in CSV format, or in rows of JSON documents \(JSON lines format\)\. Each row or document in a dataset is called a *record*\. Each labeled value or key\-value pair in a record is a *field*\. Each record much have a timestamp field and at least one field that the detector monitors, called a *measure*\.

A dataset can have live data, historical data or both\. A detector looks for anomalies in live data, and uses historical data for learning\. If its dataset has only historical data, a detector runs in *backtest mode*\. In backtest mode, a detector uses most of the data for learning and attempts to find anomalies in a smaller subset of recent data\.

Datasets have a datasource, a service role, and a mapping that tells the detector which values to monitor\. For more information, see [Managing a dataset in Amazon S3](detectors-dataset.md)\.

## Metrics<a name="gettingstarted-concepts-metrics"></a>

After choosing a datasource, you choose fields to be the dataset's measures\. *Measures* are the primary fields that the detector monitors\. You can also configure up to five additional fields as *dimensions*\. Dimensions are secondary fields that create subgroups of measures based on their value\. Each combination of metric and dimension is called a *metric*\.

For example, you can choose a field named `availability` for a measure\. If you don't choose a dimension, the detector monitors availability across all records\. If you choose a field named `country` for a dimension, then the detector monitors availability in each country as a separate metric: *availability in Canada*, *availability in Italy*, and so on\.

For more information, see [Setting up a detector](detectors-setup.md)\.

## Alert<a name="gettingstarted-concepts-alert"></a>

To send a notifications or initiate a processing workflow when the detector finds an anomaly, you can create an alert\. An alert has a target that can be an Amazon Simple Notification Service \(Amazon SNS\) topic or an AWS Lambda function\. When the detector finds an anomaly with a severity score over a configurable threshold, the alert sends a record of the anomaly to the target\.

You can process the anomaly record in the programming language of your choice with a Lambda function\. With an Amazon SNS topic, you can send the anomaly record to multiple subscribers\. A subscriber can use any protocol that Amazon SNS supports, including email addresses, mobile devices, and webhooks\. With a webhook, you can send the anomaly record to third\-party services, such as Slack\.

For more information, see [Creating alerts ](detectors-alerts.md)\.

## Feedback<a name="gettingstarted-concepts-feedback"></a>

When the detector finds an anomaly, it creates a report with details about all of the metrics that had unexpected values during the interval in the Lookout for Metrics console\. When you view this report , you can provide feedback on the relevance of each metric\. The detector uses your feedback to improve its accuracy\.

For more information, see [Viewing anomalies ](detectors-anomalies.md)\.