# Setting up a detector<a name="detectors-setup"></a>

An anomaly detector is an Amazon Lookout for Metrics resource that monitors a dataset to find anomalies\. To create a detector, you configure just a name, description, and interval\. You can then add a dataset and notifications and activate the detector to start learning and finding anomalies\.

A detector imports data from a datasource, transforms it, and stores it in a dataset\. The datasource can be an Amazon Simple Storage Service \(Amazon S3\) bucket that you store data in, a database, or another AWS service that Lookout for Metrics supports\. To get started with Amazon S3 as a datasource, see [Managing a dataset in Amazon S3](detectors-dataset.md)\. For other datasources, see [Using Amazon Lookout for Metrics with other services](lookoutmetrics-services.md)\.

Lookout for Metrics encrypts all imported data with an AWS Key Management Service \(AWS KMS\) key\. By default, the detector uses a key managed by Lookout for Metrics\. To use a key that you manage in your own account, [create a symmetric key in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) and grant Lookout for Metrics permission to use it\.

**To create a detector**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose **Create detector**\.

1. Configure the following options\.

****
   + **Name** – The detector's name\.
   + **Description** – A description of the detector\.
   + **Interval** – The amount of time between analysis attempts\.

1. \(Optional\) To choose an encryption key, check the **Customize encryption settings** box\. You cannot change the encryption key later\.

1. Choose **Create**\.

The new detector does not yet have a dataset to analyze\. To start analyzing data, create a dataset and give Lookout for Metrics permission to access it\.

**To create a dataset**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Create dataset**\.

1. Configure the following options\.

****
   + **Name** – The dataset's name\.
   + **Description** – A description of the dataset\.
   + **Timezone** – The timezone where the data is generated\. When a detector analyzes data, it verifies that each data point falls within the current interval\.

1. Choose a datasource\. The datasource can be an Amazon S3 bucket, an AWS service, or a database\.

1. Configure the datasource and then choose **Next**\. Options vary depending on the datasource that you choose\. Common settings include the following\.
   + **Interval** – The amount of time between analysis attempts\. Use the same setting as the detector's interval\.
   + **Offset** – The minimum amount of time that the detector should wait before accessing data, after the end of each interval\.
   + **Permissions** – A [service role](permissions-service.md) that gives Lookout for Metrics permission to access either the datasource or a secret that contains credentials for the datasource\.

1. Configure the metrics that the detector analyzes\.
   + **Measures** – The primary metrics that the detector analyzes to find anomalies\.
   + **Dimensions** – Secondary metrics that segment the data by, for example, location or demographic\.
   + **Timestamp** – The metric that specifies the time that the data point was created\.

1. Choose **Next**\.

1. Choose **Save and activate**\.

When you activate a detector, it starts analyzing data and learns to identify anomalies by identifying patterns in metrics\. Learning time [varies depending on the the detector's interval](gettingstarted-quotas.md#gettingstarted-quotas-coldstart) and whether you provide historical data\. With a 5 minute interval and no historical data, learning time is up to 25 hours\. During this time, the detector's status is **Initializing**\.

**Note**  
To communicate with other services, Lookout for Metrics needs permissions from an AWS Identity and Access Management \(IAM\) service role\. When you use the console to configure a dataset, you can create a service role or choose one you already have\. If you don't have permission to create roles, ask an administrator to create a service role for Lookout for Metrics\.  
For more information, see [Service roles for Amazon Lookout for Metrics](permissions-service.md)\.

The console registers the dataset and activates the detector to start learning and finding anomalies\.