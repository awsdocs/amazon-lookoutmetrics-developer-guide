# Viewing Amazon Lookout for Metrics API activity in CloudTrail<a name="monitoring-cloudtrail"></a>

Amazon Lookout for Metrics is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Lookout for Metrics\. CloudTrail captures all API calls for Lookout for Metrics as events\. Captured calls include calls from the Lookout for Metrics console and code calls to the Lookout for Metrics API operations\. 

Using the information collected by CloudTrail, you can determine the request that was made to Lookout for Metrics, the IP address from which the request was made, who made the request, when it was made, and additional details\.

All [Lookout for Metrics calls](https://docs.aws.amazon.com/lookoutmetrics/latest/api/API_Operations.html) are logged by CloudTrail\. Log entries contain information about who generated the request\. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management \(IAM\) user credentials\.
+ Whether the request was made with temporary security credentials for a role or federated user\.
+ Whether the request was made by another AWS service\.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html)\.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)\.

**Topics**
+ [Storing Lookout for Metrics information in CloudTrail](#services-cloudtrail-logs)
+ [Example: Lookout for Metrics log file entry](#services-cloudtrail-format)

## Storing Lookout for Metrics information in CloudTrail<a name="services-cloudtrail-logs"></a>

AWS CloudTrail is activated on your AWS account when you create it\. When activity occurs in Lookout for Metrics, it is automatically recorded in a CloudTrail event\. You can view, search, and download recent events in the **Event history** in the CloudTrail console\. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)\.

For an ongoing record of events in your AWS account, including events for Lookout for Metrics, create a trail\. A *trail* enables CloudTrail to send log files to an Amazon S3 bucket\. When you create a trail in the console, the trail applies to all AWS Regions\. The trail logs events from all Regions in the AWS partition\. It sends the log files to the Amazon S3 bucket that you specify\. For more information, see [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)\.



You can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs\. For more information, see the following:
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

## Example: Lookout for Metrics log file entry<a name="services-cloudtrail-format"></a>

AWS CloudTrail log files contain one or more log entries, one entry for every event\. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on\. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order\. 

The following example is a CloudTrail log entry for a `DescribeAnomalyDetector` call\. Specific information about the call appears in the `eventName` and `requestParameters` fields\. The remaining fields record details about the caller and tracking information such as the request ID, which you can use to find information about the request in places like logs and [AWS X\-Ray](https://docs.aws.amazon.com/xray/latest/devguide/) traces\.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AKIAI44QH8DHBEXAMPLE",
        "arn": "arn:aws:iam::123456789012:user/fred",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "fred",
        "sessionContext": {
            "sessionIssuer": {},
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2021-01-09T00:14:34Z"
            }
        }
    },
    "eventTime": "2021-01-09T00:18:12Z",
    "eventSource": "lookoutmetrics.amazonaws.com",
    "eventName": "DescribeAnomalyDetector",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "205.256.256.182",
    "userAgent": "aws-sdk-java/1.11.930 Linux/4.9.230-0.1.ac.223.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.275-b01 java/1.8.0_275 vendor/Oracle_Corporation",
    "requestParameters": {
        "AnomalyDetectorArn": "arn:aws:lookoutmetrics:us-east-2:123456789012:AnomalyDetector:my-detector-5m"
    },
    "responseElements": null,
    "requestID": "f587ee3c-xmpl-406b-b573-66100bb14b61",
    "eventID": "f2f879f8-xmpl-4475-9c0c-4291a389e14a",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123456789012"
}
```