# Set up a detector<a name="gettingstarted-detector"></a>

After you've [prepared data in an Amazon Simple Storage Service \(Amazon S3\) bucket](gettingstarted-datasource.md), create a detector and add a dataset\. At the end of each interval, the detector imports data from the bucket \(your datasource\) into the dataset and analyzes it\.

**Topics**
+ [Create a detector](#gettingstarted-detector-create)
+ [Add a dataset](#gettingstarted-detector-add-dataset)
+ [Activate the detector](#gettingstarted-detector-activate)
+ [\(Optional\) Add an alert](#gettingstarted-detector-alert)
+ [Review anomalies](#gettingstarted-detector-anomalies)
+ [Clean up](#gettingstarted-detector-cleanup)

## Create a detector<a name="gettingstarted-detector-create"></a>

Use the Lookout for Metrics console to create the detector that monitors your data\.

**To create a detector**

1. Open the [Lookout for Metrics console](https://console.aws.amazon.com/lookoutmetrics/home)\.

1. Choose **Create detector**\.

1. For **Name**, enter `sample-detector`\.

1. For **Description**, enter `Getting started detector`\.

1. For **Interval**, choose the interval that you used to organize your data\.

1. Choose a **Create**\.

## Add a dataset<a name="gettingstarted-detector-add-dataset"></a>

Add a dataset by specifying the location of your data in Amazon S3 and the names of fields in your data that are timestamps, measures, and dimensions\.

**To add a dataset**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors) page\.

1. Choose **sample\-detector**\.

1. Choose **Add dataset**\.

1. For **Name**, enter **S3\-dataset**\.

1. For **Timezone**, choose the timezone that is reflected in your data's timestamps\.

1. For **Datasource**, choose Amazon S3\.

1. Choose a detector mode\. For **Backtest**, you only provide historical data\. For **Continous**, you provide continuous data and can optionally provide historical data to speed up learning\.

1. Follow the instructions to specify the data path\(s\) and then choose **Next**\.

1. Choose the field in your data that specifies a timestamp for each record\. The detector checks the timestamp on each record, and only processes records that match the interval that it is analyzing\.

1. Choose a numerical field in your data to be a **Measure**\. The detector aggregates values of the measure field within each interval and monitors the aggregate value\. For example, `availability`

1. \(Optional\) Choose additional fields to be measures and dimensions\. A dimension is a field that creates subgroups of measure values that are monitored separately\. For example, `city`\.

## Activate the detector<a name="gettingstarted-detector-activate"></a>

To import data from the bucket and look for anomalies, activate the detector\.

**To activate the detector**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors) page\.

1. Choose the detector\.

1. Choose **Activate detector**\. 

When you activate the detector, it uses data from several intervals to learn, before attempting to find anomalies\. If no historical data is available, the training process takes approximately one day for a five\-minute interval\. Training time varies [depending on the detector's interval](quotas.md#gettingstarted-quotas-coldstart)\.

## \(Optional\) Add an alert<a name="gettingstarted-detector-alert"></a>

In this section, you will add an alert to the detector\. You will need to create an Amazon SNS topic\. You will use its ARN in this step\. For more information about creating an Amazon SNS topic, see [Tutorial: Creating an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-tutorial-create-topic.html)\. 

**To add an alert**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Add alert**\.

1. Configure the following options\.

****
   + **Name** – `my-alert`
   + **Description** – `Send anomaly alerts to an SNS topic.`
   + **Threshold** – `50`
   + **Channel** – Amazon SNS
   + **Resource** – Your SNS topic
   + **Role** – **Create a role**

1. Choose **Add alert**\.

## Review anomalies<a name="gettingstarted-detector-anomalies"></a>

In this section, you will review the anomalies found by the detector\. 

**To review anomalies**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors) page\.

1. Choose **sample\-detector**\.

1. Choose **View anomalies**\. 

1. Choose an anomaly\.

Each anomaly can have multiple metrics associated with it\. Review each metric to see if it is relevant or not, and use the feedback options to help the detector learn about your data\.

## Clean up<a name="gettingstarted-detector-cleanup"></a>

If you are done using the detector, delete it\.

**To delete the detector**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors) page\.

1. Choose the detector, **sample\-detector**\.

1. Choose **Delete**\.

The detector's dataset and alerts are deleted automatically\.
