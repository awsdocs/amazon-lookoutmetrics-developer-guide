# Lookout for Metrics quotas<a name="gettingstarted-quotas"></a>

Amazon Lookout for Metrics sets quotas for the amount of data that a detector can use to learn and detect anomalies\. There are also quotas for data import intervals, records processing, and Amazon Lookout for Metrics API requests\. Additionally, there are data requirements for data retention for re\-training, coldstart anomaly detection, backtesting, time series, and record field key value pairs\.

**Note**  
The quotas listed on this page are for the preview release of Lookout for Metrics\. Quota values and scope might change prior to general availability\.

Quotas set by other services can impact operation\. For information on quotas for other services such as Amazon CloudWatch, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) in the *Amazon Web Services General Reference*\.

**Topics**
+ [Adjustable quotas](#gettingstarted-quotas-adjustable)
+ [Fixed quotas](#gettingstarted-quotas-fixed)
+ [Data retention time periods for re\-training](#gettingstarted-quotas-retention)
+ [Coldstart anomaly detection](#gettingstarted-quotas-coldstart)
+ [Backtesting data requirements](#gettingstarted-quotas-backtest)
+ [Record field key\-value pair character limits](#gettingstarted-quotas-fields)

## Adjustable quotas<a name="gettingstarted-quotas-adjustable"></a>

 The following quotas can be increased\. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*\.


| Resource | Default quota | 
| --- |--- |
| Quotas for detectors | 
| --- |
| Maximum number of detectors | 10 | 
| Maximum number of alerts for a detector | 10 | 
| Quotas for datasets | 
| --- |
| Maximum number of dimensions for a dataset | 5 dimensions | 
| Maximum number of measures for a dataset | 5 measures | 
| Quotas for historical data | 
| --- |
| Maximum intervals \(continous mode\) | 2500 | 
| Maximum intervals \(backtest mode\) | 3000 | 
| Maximum number of files you can upload per interval | 
| --- |
| 5\-minute interval | 5 files | 
| 10\-minute interval | 5 files | 
| 1\-hour interval | 10 files | 
| 1\-day interval | 10 files | 
| Maximum number of records Lookout for Metrics can process per interval | 
| --- |
| 5\-minute interval | 15000 records | 
| 10\-minute interval | 24000 records | 
| 1\-hour interval | 150000 records | 
| 1\-day interval | 300000 records | 
| Maximum number of metrics Lookout for Metrics can process per interval | 
| --- |
| 5\-minute interval | 5000 metrics | 
| 10\-minute interval | 10000 metrics | 
| 1\-hour interval | 50000 metrics | 
| 1\-day interval | 50000 metrics | 

The following adjustable Lookout for Metrics quotas apply per AWS Region and are for Lookout for Metrics API requests\.


| Resource | Default Quota | 
| --- | --- | 
| Maximum rate of total API requests |  20/second  | 
| Maximum rate of CreateAnomalyDetector API requests |  1/second  | 
| Maximum rate of UpdateAnomalyDetector API requests |  1/second  | 
| Maximum rate of DeleteAnomalyDetector API requests |  1/second  | 
| Maximum rate of ListAnomalyDetectors API requests |  2/second  | 
| Maximum rate of DescribeAnomalyDetector API requests |  2/second  | 
| Maximum rate of ActivateAnomalyDetector API requests |  1/second  | 
| Maximum rate of BackTestAnomalyDetector API requests |  1/second  | 
| Maximum rate of DescribeAnomalyDetectionExecutions API requests |  2/second  | 
| Maximum rate of ListAnomalyGroupSummaries API requests |  2/second  | 
| Maximum rate of ListAnomalyGroupTimeSeries API requests |  2/second  | 
| Maximum rate of GetAnomalyGroup API requests |  2/second  | 
| Maximum rate of CreateMetricSet API requests |  1/second  | 
| Maximum rate of DescribeMetricSet API requests |  2/second  | 
| Maximum rate of ListMetricSets API requests |  2/second  | 
| Maximum rate of UpdateMetricSet API requests |  1/second  | 
| Maximum rate of CreateAlert API requests |  1/second  | 
| Maximum rate of DeleteAlert API requests |  1/second  | 
| Maximum rate of DescribeAlert API requests |  2/second  | 
| Maximum rate of ListAlerts API requests |  2/second  | 
| Maximum rate of GetDataQualityMetrics API requests |  2/second  | 
| Maximum rate of GetSampleData API requests |  2/second  | 
| Maximum rate of PutFeedback API requests |  1/second  | 
| Maximum rate of GetFeedback API requests |  2/second  | 
| Maximum rate of RunAnomalyDetection API requests per anomaly detector |  1/second  | 
| Maximum rate of TrainAnomalyDetector API requests per anomaly detector |  1/second  | 

## Fixed quotas<a name="gettingstarted-quotas-fixed"></a>

The following quotas cannot be changed\.


| Resource | Quota | 
| --- | --- | 
| Maximum number of datasets for a detector | 1 dataset | 
| Maximum number of data sources for a dataset | 1 datasource | 
| Maximum length of a field value in a data point | 40 bytes | 

## Data retention time periods for re\-training<a name="gettingstarted-quotas-retention"></a>

 The amount of time you should retain your data for re\-training depends on the interval of your data collection as follows: 


| Interval | Maximum time | Average time | 
| --- | --- | --- | 
| 5 minutes | 9 days | 4\.5 days | 
| 10 minutes | 18 days | 9 days | 
| 1 hour | 3\.4 months | 2 months | 
| 1 day | 5 years | 2 years | 

## Coldstart anomaly detection<a name="gettingstarted-quotas-coldstart"></a>

 For coldstart anomaly detection \(no historical data\), the amount of time it takes for Lookout for Metrics to detect anomalies depends on the interval of your data collection as follows: 
+  **5 minute interval** – 25 hours
+  **10 minute interval** – 50 hours
+  **1 hour interval** – 12\.5 days
+  **1 day interval** – 14 days

## Backtesting data requirements<a name="gettingstarted-quotas-backtest"></a>

 The ratio of training and testing data used for backtesting is 70% training and 30% testing\. The maximum number of data points you will see is 900, and the number of days of data Lookout for Metrics considers for backtesting depends on the interval of your data collection as follows: 
+  **5 minute interval** – 3\.125 days, with 12 data points per hour and 288 data points per day\. 
+  **10 minute interval** – 6\.25 days, with 6 data points per hour and 144 data points per day\. 
+  **1 hour interval** – 37\.5 days, with 1 data point per hour and 24 points per day\. 
+  **1 day interval** – 900 days, with 1 data point per day\. 

 The minimum amount of data required for backtesting depends on the interval of your data collection as follows: 
+  **5 minute interval** – \~1 day of data\. 
+  **10 minute interval** – 1\.9 days of data\. 
+  **1 hour interval** – 11\.8 days of data\. 
+  **1 day interval** – 285 days of data\. 

## Record field key\-value pair character limits<a name="gettingstarted-quotas-fields"></a>

 Character limits for record field key value pairs are as follows: 
+ Dimensions key – 63 characters
+ Dimension value – 50 characters
+ Timestamp key – 63 characters
+ Measure value – 10^15 with precision of 4 after decimal point