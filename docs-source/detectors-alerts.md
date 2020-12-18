# Creating alerts<a name="detectors-alerts"></a>

Amazon Lookout for Metrics detectors find anomalies in data\. When an anomaly is severe, the detector can send details about it to another AWS service or resource\. You can configure a detector to run an AWS Lambda function to process anomaly alerts, or send details to an Amazon Simple Notification Service \(Amazon SNS\) topic\. Amazon SNS can then send the information to email subscribers or an HTTP endpoint, among numerous other supported destinations\.

To send anomaly alerts, a detector uses a [service role](permissions-service.md)\. When you use the console to create alerts, you can create a service role or choose one you already have\. If you don't have permission to create roles, ask an administrator to create a service role for Lookout for Metrics\.

**To create an alert**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Add alert**\.

1. Configure the following options\.

****
   + **Name** – The name of the alert\.
   + **Description** – A description of the alert\.
   + **Threshold** – The severity score that the anomaly must reach for the detector to send an anomaly alert\.
   + **Channel** – The destination service\.
   + **Resource** – The resource in the target service that receives the anomaly alert\.
   + **Role** – A service role that allows the detector to send alerts to the resource\.

1. Choose **Create**\.

The configurable threshold determines when the detector sends anomaly alerts\. If you get anomaly alerts for anomalies that are not severe, you can increase the threshold\. If you don't get enough alerts, you can lower it\.