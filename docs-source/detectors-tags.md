# Tagging Lookout for Metrics resources<a name="detectors-tags"></a>

Organize your Amazon Lookout for Metrics resources by owner, project or department with tags\. Tags are key\-value pairs that are supported across AWS services\. You can use tags to filter resources, create least\-privilege permissions policies, and add detail to billing reports\. Lookout for Metrics also supports tag\-based authorization\. With tag\-based authorization, you can create [permissions policies](permissions-user.md) that limit a user's access to resources with specific tags\. For more information about tag\-based authorization, see [Controlling access to AWS resources using resource tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *IAM User Guide*\.

You can add tags to [detectors](lookoutmetrics-detectors.md), [datasets](detectors-dataset.md), and [alerts](detectors-alerts.md) when you create them, or you can add tags to existing resources\. You can use the Lookout for Metrics console or manage tags with the [Lookout for Metrics API](#detectors-tags-api)\. Start by tagging your detectors to organize them into logical groups\.

For more information about tags, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws-tagging.html) in the *Amazon Web Services General Reference*\.

**To add tags to a detector in the Lookout for Metrics console**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Tags**\.

1. Choose **Manage tags**\.

1. Enter a key and value\. For example, `Department` and `Marketing`\.

1. To add additional tags, choose **Add tag**\.

1. Choose **Save**\.

Tags apply to each detector, dataset, and alert individually\. They are not shared or inherited\.

**Topics**
+ [Using tags \(Lookout for Metrics API\)](#detectors-tags-api)
+ [Tag key and value requirements](#detectors-tags-requirements)

## Using tags \(Lookout for Metrics API\)<a name="detectors-tags-api"></a>

When you create resources with the [CreateAnomalyDetector](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_CreateAnomalyDetector.html), [CreateMetricSet](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_CreateMetricSet.html) and [CreateAlert](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_CreateAlert.html) operations, you can include tags with the `--tags` option\. The following example shows how to apply tags when creating an anomaly detector with the AWS Command Line Interface \(AWS CLI\)\.

```
$ aws lookoutmetrics create-anomaly-detector --anomaly-detector-name my-detector \
  --anomaly-detector-config AnomalyDetectorFrequency=PT10M \ 
  --anomaly-detector-description "10-minute S3 detector" \
  --tags Department=Marketing,CostCenter=1234ABCD
{
    "AnomalyDetectorArn": "arn:aws:lookoutmetrics:us-east-2:123456789012:AnomalyDetector:my-detector"
}
```

To add tags to an existing resource, use the [TagResource](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_TagResource.html) operation\.

```
$ aws lookoutmetrics tag-resource --resource-arn arn:aws:lookoutmetrics:us-east-2:123456789012:AnomalyDetector:my-detector \
  --tags Department=Marketing,CostCenter=1234ABCD
```

To remove tags, use the [UntagResource](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_UntagResource.html) operation\.

```
$ aws lookoutmetrics untag-resource --resource-arn  arn:aws:lookoutmetrics:us-east-2:123456789012:AnomalyDetector:my-detector \
  --tag-keys Department
```

To view tags, you can use the following API operations:
+ [ListTagsForResource](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ListTagsForResource.html) – View the tags associated with a resource\.

  ```
  $ aws lookoutmetrics list-tags-for-resource --resource-arn arn:aws:lookoutmetrics:us-east-2:123456789012:AnomalyDetector:my-detector
  {
      "Tags": {
          "Department": "Marketing",
          "CostCenter": "1234ABCD"
      }
  }
  ```
+ [ListAnomalyDetectors](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ListAnomalyDetectors.html), [ListMetricSets](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ListMetricSets.html), [ListAlerts](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_ListAlerts.html) – Get a list of resources with tag information\.

  ```
  $ aws lookoutmetrics list-anomaly-detectors
  {
      "AnomalyDetectorSummaryList": [
          {
              "Status": "INACTIVE",
              "AnomalyDetectorName": "my-detector",
              "Tags": {
                  "Department": "Marketing",
                  "CostCenter": "1234ABCD"
              },
              "LastModificationTime": 1612994728.528,
              "CreationTime": 1612994728.528,
              "AnomalyDetectorArn": "arn:aws:lookoutmetrics:us-east-2:123456789012:AnomalyDetector:my-detector"
          }
      ]
  }
  ```

## Tag key and value requirements<a name="detectors-tags-requirements"></a>

The following requirements apply to tags for Lookout for Metrics resources:
+ Maximum number of tags per resource – 50
+ Maximum key length – 128 Unicode characters in UTF\-8
+ Maximum value length – 256 Unicode characters in UTF\-8
+ Tag keys and values are case sensitive\.
+ Your tag keys and values can't start with `aws:`\. AWS services apply tags that start with `aws:`, and those tags can't be modified\. They don't count towards tag limits\.
+ Tag keys and values can contain the following characters: A\-Z, a\-z, 0\-9, space, and \_ \. : / = \+ @ \- \(hyphen\)\. This is the standard set of characters available across AWS services that support tags\. Some services support additional symbols\.