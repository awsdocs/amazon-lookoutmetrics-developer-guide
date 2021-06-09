# Using Amazon S3 with Lookout for Metrics<a name="services-s3"></a>

You can use Amazon Simple Storage Service \(Amazon S3\) as a datasource for an Amazon Lookout for Metrics detector\. With Amazon S3, you provide data in a bucket organized into separate folders for each interval\. You configure the detector with a pattern that indicates where to find data for each interval, and write data to the path of the current interval as it is generated\.

For example, if your detector's interval is 1 day, then you write data to a separate path for each day, in a predictable pattern\. For example, the data for January 2nd, 2021 can go in a folder named `2021/01/02`, `2021-01/02`, `20210102`, etc\.

Your data can consist of rows of delimited records \(CSV format\) or JSON objects \(JSON lines format\)\. Each line in a file has one record, which has fields for measures, dimensions, and a timestamp\. For details on organizing and formatting your data, see [Managing a dataset in Amazon S3](detectors-dataset.md)\.

The detector imports data at the end of each interval\. You configure an **offset** to allow time after an interval ends for all data to be written\. For example, if you choose an offset of 30 seconds, the detector waits 30 seconds after the end of each interval before reading data for that interval\.

**To create an Amazon S3 dataset**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Add dataset**\.

1. Choose **Amazon S3**\.

1. Follow the instructions to create the datasource\.

The detector reads new data from Amazon S3 periodically, by getting objects from the folder for the most recent completed interval\. If it detects any anomalies in the metrics for the interval, it records an anomaly and sends [anomaly alerts](detectors-alerts.md), if configured\.

When you activate the detector, it uses data from several intervals to learn, before attempting to find anomalies\. If no historical data is available, the training process takes approximately one day for a five\-minute interval\. Training time varies [depending on the detector's interval](quotas.md#gettingstarted-quotas-coldstart)\.

For more information about Amazon S3, see [Getting started with Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html) in the Amazon Simple Storage Service Getting Started Guide\.



**Topics**
+ [Configuring permissions](#services-s3-permissions)
+ [Structuring data](#services-s3-structure)
+ [Timestamps](#services-s3-timestamp)
+ [Running a backtest](#services-s3-backtest)

## Configuring permissions<a name="services-s3-permissions"></a>

When you add an Amazon S3 dataset to your detector, the Lookout for Metrics console creates a [service role](permissions-service.md) with permission to read data from the bucket, and permission to use AWS Key Management Service \(AWS KMS\) to encrypt and decrypt data\.

The console creates a role for the dataset, and a separate role for each alert that you configure\. You can create a single role for the detector that gives it all of the permissions that it needs\. To use a custom role, create an IAM role that Lookout for Metrics has permission to assume, and add permission to use Amazon S3 and AWS KMS\.

## Structuring data<a name="services-s3-structure"></a>

To determine the correct pattern for your data, you can enter the URI of any example data file in the bucket\. The console analyzes the path and shows one or more patterns that matches\. Choose the pattern that matches your folder structure\.

For details on organizing your data, see [Managing a dataset in Amazon S3](detectors-dataset.md)\.

## Timestamps<a name="services-s3-timestamp"></a>

Entries in your data must have a field with a date or timestamp that indicates which interval they occur in\. When you configure your dataset, you specify the format of the timestamp as a pattern with the following keys\.

****
+ `yyyy` – Year
+ `MM` – Month
+ `DD` – Day
+ `HH` – Hour \(24\-hour time\)
+ `hh` – Hour \(12\-hour time\)
+ `a` – AM/PM indicator \(with 12\-hour `hh` key\)
+ `mm` – Minutes
+ `ss` – Seconds

For daily intervals, you can use a date that indicates only the day\. For more granular intervals, the timestamp must be specific enough to distinguish between intervals\.

****
+ `yyyy-MM-DD` – `2021-02-28` \(daily only\)
+ `yyyy-MM-DD HH:mm:ss` – `2021-02-28 17:45:32` \(any interval\)
+ `yyyy-MM-dd hh:mm:ss a` – `2021-02-28 05:45:32 pm` \(any interval\)

## Running a backtest<a name="services-s3-backtest"></a>

In backtest mode, a detector uses historical data to learn and find anomalies\. You provide recent data for a large number of intervals at a single path\. In backtest mode, Lookout for Metrics splits historical data into two subsets\. 70 percent of the data is used to train the detector\. The detector then analyzes the other 30 percent to identify anomalies\. You can use test mode to validate the detector's results and verify its accuracy\.

For backtest mode, you can provide between 285 and 3000 intervals worth of data\. The data can be in one file or multiple files in the same folder\. This gives the detector at least 200 intervals of data to learn with\. The detector always uses older data for learning and newer data for testing\.