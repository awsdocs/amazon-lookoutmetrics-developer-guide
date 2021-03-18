# Data protection in Amazon Lookout for Metrics<a name="security-dataprotection"></a>

The AWS [shared responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon Lookout for Metrics\. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud\. You are responsible for maintaining control over your content that is hosted on this infrastructure\. This content includes the security configuration and management tasks for the AWS services that you use\. For more information about data privacy, see the [Data Privacy FAQ](http://aws.amazon.com/compliance/data-privacy-faq)\. For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/) blog post on the *AWS Security Blog*\.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual user accounts with AWS Identity and Access Management \(IAM\)\. That way each user is given only the permissions necessary to fulfill their job duties\. We also recommend that you secure your data in the following ways:
+ Use multi\-factor authentication \(MFA\) with each account\.
+ Use SSL/TLS to communicate with AWS resources\. We recommend TLS 1\.2 or later\.
+ Set up API and user activity logging with AWS CloudTrail\.
+ Use AWS encryption solutions, along with all default security controls within AWS services\.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing personal data that is stored in Amazon S3\.
+ If you require FIPS 140\-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint\. For more information about the available FIPS endpoints, see [Federal Information Processing Standard \(FIPS\) 140\-2](http://aws.amazon.com/compliance/fips/)\.

We strongly recommend that you never put sensitive identifying information, such as your customers' account numbers, into free\-form fields such as a **Name** field\. This includes when you work with Lookout for Metrics or other AWS services using the console, API, AWS CLI, or AWS SDKs\. Any data that you enter into Lookout for Metrics or other services might get picked up for inclusion in diagnostic logs\. When you provide a URL to an external server, don't include credentials information in the URL to validate your request to that server\.

**Topics**
+ [Encryption in transit](#security-privacy-intransit)
+ [Encryption at rest](#security-privacy-atrest)

## Encryption in transit<a name="security-privacy-intransit"></a>

Lookout for Metrics API endpoints support secure connections only over HTTPS\. When you manage Lookout for Metrics resources with the AWS Management Console, AWS SDK, or the Lookout for Metrics API, all communication is encrypted with Transport Layer Security \(TLS\)\.

For a complete list of API endpoints, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the* AWS General Reference\.*

## Encryption at rest<a name="security-privacy-atrest"></a>

Lookout for Metrics always encrypts a detector's dataset at rest\. Additionally, you can [configure Lookout for Metrics to use an encryption key](detectors-manage.md) that you create and manage in AWS Key Management Service\. These are referred to as *customer managed* customer master keys \(CMKs\) or customer managed keys\. If you don't configure a customer managed key, Lookout for Metrics uses a key that the service manages\.

Additionally, Lookout for Metrics encrypts your resources' configuration at rest with a key that it manages\. This includes the names of fields or columns in your datasource that you use as [measures and dimensions](gettingstarted-concepts.md#gettingstarted-concepts-metrics)\. You can't configure Lookout for Metrics to use a CMK for configuration data\.