# AWS managed policies for Amazon Lookout for Metrics<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself\. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need\. To get started quickly, you can use our AWS managed policies\. These policies cover common use cases and are available in your AWS account\. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*\.

AWS services maintain and update AWS managed policies\. You can't change the permissions in AWS managed policies\. Services occasionally add additional permissions to an AWS managed policy to support new features\. This type of update affects all identities \(users, groups, and roles\) where the policy is attached\. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available\. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions\.

Additionally, AWS supports managed policies for job functions that span multiple services\. For example, the **ReadOnlyAccess** AWS managed policy provides read\-only access to all AWS services and resources\. When a service launches a new feature, AWS adds read\-only permissions for new operations and resources\. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*\.

## Managed policy: AmazonLookoutMetricsReadOnlyAccess<a name="security-iam-awsmanpol-ReadOnlyAccess"></a>

The AmazonLookoutMetricsReadOnlyAccess managed policy grants *read\-only* permissions that allow read\-only access to all Lookout for Metrics resources\. You can attach this policy to your IAM entities\. 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lookoutmetrics:DescribeMetricSet",
        "lookoutmetrics:ListMetricSets",
        "lookoutmetrics:DescribeAnomalyDetector",
        "lookoutmetrics:ListAnomalyDetectors",
        "lookoutmetrics:DescribeAnomalyDetectionExecutions",
        "lookoutmetrics:DescribeAlert",
        "lookoutmetrics:ListAlerts",
        "lookoutmetrics:ListTagsForResource",
        "lookoutmetrics:ListAnomalyGroupSummaries",
        "lookoutmetrics:ListAnomalyGroupTimeSeries",
        "lookoutmetrics:GetAnomalyGroup",
        "lookoutmetrics:GetDataQualityMetrics",
        "lookoutmetrics:GetSampleData",
        "lookoutmetrics:GetFeedback"
      ],
      "Resource": "*"
    }
  ]
}
```

## Managed policy: AmazonLookoutMetricsFullAccess<a name="security-iam-awsmanpol-FullAccess"></a>

The AmazonLookoutMetricsFullAccess managed policy grants full access to Lookout for Metrics resources, and permission to assign a service role to a detector\. You can attach this policy to your IAM entities\. A *service role* is an IAM role that grants permissions to an AWS service so it can access resources\. Service roles must be created by an administrator

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lookoutmetrics:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:PassRole"
      ],
      "Resource": "arn:aws:iam::*:role/*LookoutMetrics*",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "lookoutmetrics.amazonaws.com"
        }
      }
    }
  ]
}
```

## Lookout for Metrics updates to AWS managed policies<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Lookout for Metrics since this service began tracking these changes\.


| Change | Description | Date | 
| --- | --- | --- | 
|  [AmazonLookoutMetricsReadOnlyAccess](#security-iam-awsmanpol-ReadOnlyAccess) – New policy  |  Lookout for Metrics added a new policy to allow read\-only access for all Lookout for Metrics resources\.  | May 06, 2021 | 
|  [AmazonLookoutMetricsFullAccess](#security-iam-awsmanpol-FullAccess) – New policy  | Lookout for Metrics added a new policy to allow full access to all Lookout for Metrics resources\. | May 06, 2021 | 
|  Lookout for Metrics started tracking changes  |  Lookout for Metrics started tracking changes for its AWS managed policies\.  | May 06, 2021 | 