# Amazon Lookout for Metrics permissions<a name="lookoutmetrics-permissions"></a>

You can use AWS Identity and Access Management \(IAM\) to manage access to the Lookout for Metrics API and resources like detectors and datasets\. For users and applications in your account that use Lookout for Metrics, you manage permissions in a permissions policy that you can apply to IAM users, groups, or roles\.

To manage permissions for users and applications in your accounts, [use the managed policies that Lookout for Metrics provides](permissions-user.md), or write your own\. The Lookout for Metrics console uses multiple services to get information about your function's configuration and triggers\. You can use the managed policies as\-is, or as a starting point for more restrictive policies\.

Lookout for Metrics uses IAM [service roles](permissions-service.md) to access other services on your behalf\. You create or choose a service role when you create a dataset that reads data from Amazon S3 or another service\. You also pass service roles to Lookout for Metrics when you configure an alert that targets a Lambda function or an Amazon SNS topic\. The Lookout for Metrics console can create these roles for you if you have the required IAM permissions\.

For more information about IAM, see [What is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in the *IAM User Guide*\.

**Topics**
+ [Identity\-based IAM policies for Lookout for Metrics](permissions-user.md)
+ [Service roles for Amazon Lookout for Metrics](permissions-service.md)