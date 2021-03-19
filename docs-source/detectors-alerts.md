# Working with alerts<a name="detectors-alerts"></a>

Amazon Lookout for Metrics detectors find anomalies in data\. When an anomaly is severe, the detector can send details about it to another AWS service or resource\. You can configure a detector to run an AWS Lambda function to process anomaly alerts, or send details to an Amazon Simple Notification Service \(Amazon SNS\) topic\. Amazon SNS can then send the information to email subscribers or an HTTP endpoint, among numerous other supported destinations\.

A severity threshold determines when the detector sends anomaly alerts\. If you get anomaly alerts for anomalies that are not interesting, you can increase the threshold\. If you don't get enough alerts, you can lower it\.

To send anomaly alerts, a detector uses a [service role](permissions-service.md)\. When you use the console to create alerts, you can create a service role or choose one you already have\. If you don't have permission to create roles, ask an administrator to create a service role for Lookout for Metrics\.

**To create an alert**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Add alert**\.

1. Configure the following options\.

****
   + **Alert name** – The name of the alert\. Alert names must be unique across all detectors in a Region\.
   + **Description** – A description of the alert\.
   + **Severity threshold** – The severity score that the anomaly must reach for the detector to send an anomaly alert\.
   + **Channel** – The destination service\.
   + **SNS topic** or **Lambda function** – The resource in the target service that receives the anomaly alert\.
   + **Role** – A service role that allows the detector to send alerts to the resource\.

1. Choose **Create**\.

When the detector finds an anomaly that meets the severity threshold, it sends an anomaly alert\. An anomaly alert is a JSON document with details about the metrics that were affected by the anomaly\. The following example shows an anomaly alert where `revenue` is affected on the `pc_web` platform in two marketplaces, `it` \(Italy\) and `fr` \(France\)\.

**Example alert \(line endings and indentation added\)**  

```
{
    "alertName": "sns-alert",
    "alertEventId": "arn:aws:lookoutmetrics:us-east-2:123456789012:Alert:sns-alert:event/61975451-xmpl-4639-a133-8a060535fc08",
    "anomalyDetectorArn": "arn:aws:lookoutmetrics:us-east-2:123456789012:AnomalyDetector:my-detector",
    "alertArn": "arn:aws:lookoutmetrics:us-east-2:123456789012:Alert:sns-alert",
    "alertDescription": "SNS alert for email notifications.",
    "impactedMetric": {
        "metricName": "revenue",
        "dimensionContribution": [
            {
                "dimensionName": "marketplace",
                "dimensionValueContributions": [
                    {
                        "dimensionValue": "it",
                        "valueContribution": 73
                    },
                    {
                        "dimensionValue": "fr",
                        "valueContribution": 27
                    }
                ]
            },
            {
                "dimensionName": "platform",
                "dimensionValueContributions": [
                    {
                        "dimensionValue": "pc_web",
                        "valueContribution": 100
                    }
                ]
            }
        ],
        "relevantTimeSeries": [
            {
                "timeSeriesId": "d488c9xmpl2e46c53e73ee853cc6258e499897c4b59d595805d28fb0d290d717bc57f10ca41df45de4063f5a8491e07d23c2c26ad1c6535c69ba96264b79b60f",
                "dimensions": [
                    {
                        "dimensionName": "marketplace",
                        "dimensionValue": "it"
                    },
                    {
                        "dimensionName": "platform",
                        "dimensionValue": "pc_web"
                    }
                ],
                "metricValue": 148.5
            },
            {
                "timeSeriesId": "950feacxmpl22866d1f128991cf722b03f88f62f91770000af4b09bddb13d54691ce26346b03383d0c5c67bfc11a6c61853b71eee1c0ca47fb144f9caf5af39a",
                "dimensions": [
                    {
                        "dimensionName": "marketplace",
                        "dimensionValue": "fr"
                    },
                    {
                        "dimensionName": "platform",
                        "dimensionValue": "pc_web"
                    }
                ],
                "metricValue": 230.1
            }
        ]
    },
    "timestamp": "2021-02-14T04:00Z[Atlantic/St_Helena]",
    "anomalyScore": 86.78
}
```

In the preceding example, the detector identified unusually high revenue values \(148\.5 and 230\.1\) in Italy and France for customers using the website on a PC\. The value for Italy was farther from the expected value, so its contribution to the anomaly \(73%\) is greater than the value for France\. Overall, the anomaly for the two metrics had an severity score of 86\.78\.

The severity score is a measurement of how unexpected the observed metric values are based on the detector's understanding of your data\. It takes into consideration when the anomaly occurred, such as the time of day, and how many metrics were affected\.

As the detector learns more about your data, anomalies for similar events might have higher or lower severity scores\. You can guide its learning by providing feedback on affected metrics in an anomaly\. For more information, see [Working with anomalies](detectors-anomalies.md)\.