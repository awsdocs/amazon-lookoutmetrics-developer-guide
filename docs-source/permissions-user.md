# Identity\-based IAM policies for Lookout for Metrics<a name="permissions-user"></a>

To grant users in your account access to Lookout for Metrics, you use identity\-based policies in AWS Identity and Access Management \(IAM\)\. Identity\-based policies can apply directly to IAM users, or to IAM groups and roles that are associated with a user\. You can also grant users in another account permission to assume a role in your account and access your Lookout for Metrics resources\.

The following IAM policy allows a user to access all Lookout for Metrics API actions, and to pass [service roles](permissions-service.md) to Lookout for Metrics\.

**Example User policy**  

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
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "lookoutmetrics.amazonaws.com"
        }
      }
    }
  ]
}
```

The preceding policy does not allow a user to create IAM roles\. For a user with these permissions to create a dataset or alert, an administrator must create the service role that grants Lookout for Metrics permission to access datasources and alert channels\. For more information, see [Service roles for Amazon Lookout for Metrics](permissions-service.md)\.

In addition to Lookout for Metrics, a user needs permission to view resources in services that they use as a detector's datasource or as alert channels\. When you work with a detector in the Lookout for Metrics console, the console uses your permissions to simplify the configuration process\.

For details on the services that Lookout for Metrics supports, see [Using Amazon Lookout for Metrics with other services](chapter-services.md)\.