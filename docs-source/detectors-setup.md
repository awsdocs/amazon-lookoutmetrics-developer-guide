# Setting up a detector<a name="detectors-setup"></a>

When you create a detector, you configure just a name, description, and interval\. You can then add a dataset and notifications and activate the detector to start learning and finding anomalies\.

When you activate a detector, it starts analyzing data and learns to identify anomalies by identifying patterns between metrics\. The learning process can take up to two days\. During this time, the detector's status is **Initializing**\.

**To create a detector**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose **Create detector**\.

1. Configure the following options\.

****
   + **Name** – The detector's name\.
   + **Description** – A description of the detector\.
   + **Interval** – The amount of time between analysis attempts\.

1. \(Optional\) To choose an encryption key, check the **Customize encryption settings** box\. Lookout for Metrics must have permission to use the key\. If you don't choose a key, Lookout for Metrics uses its own key\. You cannot change the encryption key later\.

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

1. Choose a datasource\. The datasource can be text files in an Amazon S3 bucket, an AWS service, or a database\.

1. Configure the datasource and then choose **Next**\.

1. Configure the metrics that the detector analyzes\.
   + **Measures** – The primary metrics that the detector analyzes to find anomalies\.
   + **Dimensions** – Secondary metrics that segment the data by, for example, location or demographic\.
   + **Timestamp** – The metric that specifies the time that the data point was created\.

1. Choose **Next**\.

1. Choose **Save and activate**\.

**Note**  
To communicate with other services, Lookout for Metrics needs permissions from an AWS Identity and Access Management \(IAM\) service role\. When you use the console to configure a dataset, you can create a service role or choose one you already have\. If you don't have permission to create roles, ask an administrator to create a service role for Lookout for Metrics\.  
For more information, see [Service roles for Amazon Lookout for Metrics](permissions-service.md)\.

The console registers the dataset and activates the detector to start learning and finding anomalies\.