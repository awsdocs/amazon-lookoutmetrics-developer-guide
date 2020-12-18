# Identity\-based IAM policies for Lookout for Metrics<a name="permissions-user"></a>

To grant users in your account access to Lookout for Metrics, you use identity\-based policies in AWS Identity and Access Management \(IAM\)\. Identity\-based policies can apply directly to IAM users, or to IAM groups and roles that are associated with a user\. You can also grant users in another account permission to assume a role in your account and access your Lookout for Metrics resources\.

Lookout for Metrics provides managed policies that grant access to Lookout for Metrics API actions and, in some cases, access to other services used to develop and manage Lookout for Metrics resources\. Lookout for Metrics updates the managed policies as needed, to ensure that your users have access to new features when they're released\.
+ **AmazonLookoutforMetricsFullAccess** – Grants full access to Lookout for Metrics actions and other services used to develop and maintain Lookout for Metrics resources\.

Managed policies grant permission to API actions without restricting the resources that a user can modify\. For finer\-grained control, you can create your own policies that limit the scope of a user's permissions\.

At a minimum, an Lookout for Metrics user needs permission to use the following services in addition to Lookout for Metrics:
+ Data sources – Lookout for Metrics uses your permissions to access data in the service where it is stored, such as Amazon Simple Storage Service \(Amazon S3\) or Amazon CloudWatch\.
+ Alert targets – You can configure Lookout for Metrics to send alerts to an Amazon SNS topic or Lambda function\. To configure alerts, you need to pass a service role to Lookout for Metrics\. If the role already exists, you just need the `iam:PassRole` permission\. Otherwise, you need permission to create the role \(admin privileges\)\.