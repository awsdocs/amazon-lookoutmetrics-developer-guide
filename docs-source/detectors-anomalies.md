# Viewing anomalies<a name="detectors-anomalies"></a>

An *anomaly* is a data point that is unexpected based on the detector's understanding of the dataset\. The detector trains itself over time to more accurately identify anomalies based on patterns in your data\. 

The detector assigns a severity score between 0 and 100\. The severity score indicates how far the data point is outside of the expected range based on the data that the detector has analyzed\. 

**To view anomalies**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Anomalies**\.

You can filter the list of anomaly shows by adjusting the threshold\. Reduce the threshold to show more anomalies, or increase it to show fewer\.