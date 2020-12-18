# Managing detectors<a name="detectors-manage"></a>

You manage [detectors](lookoutmetrics-detectors.md) in the Lookout for Metrics console\. 

When you create a detector, you configure just a name, description, and interval\. Optionally, you can choose an encryption key to use with the dataset's data, instead of the service's default key\. After the detector is created, you can [add a dataset](detectors-dataset.md) and activate the detector to start finding anomalies\.

When activation is complete, the detector analyzes data after each interval\. If there are any anomalies in the data for an interval, the detector assigns each a severity score\. If the score exceeds an alert target's threshold, the detector sends an alert to that target\. You can view the results of each analysis in the detector log\.

To stop analyzing data and delete it from Lookout for Metrics, delete the detector\. This also deletes the detector's dataset and alerts\.

**To delete a detector**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Delete**\.

You can't recover a deleted detector or its subresources\. Data stored in Amazon Lookout for Metrics is completely deleted within 90 days of the detector being deleted\.