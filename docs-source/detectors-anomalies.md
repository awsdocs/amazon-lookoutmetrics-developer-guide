# Viewing anomalies<a name="detectors-anomalies"></a>

To get details about anomalies that a detector finds in your data, view them in the Amazon Lookout for Metrics console\.

**To view anomalies**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Anomalies**\.

1. For details, choose an anomaly from the list\.

An *anomaly* is a data point that is unexpected based on the detector's understanding of your data\. A detector learns over time to more accurately identify anomalies based on patterns that it finds\. Anomalies that occur close together are organized into groups and displayed as a single event\.

The detector assigns a severity score between 0 and 100\. The severity score indicates how far the data point is outside of the expected range based on the data that the detector has analyzed\. The higher the severity score, the more unexpected it is\.

You can filter the list of anomaly shows by adjusting the threshold\. Reduce the threshold to show more anomalies, or increase it to show fewer\.