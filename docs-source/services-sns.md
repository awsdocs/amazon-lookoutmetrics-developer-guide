# Using Amazon SNS with Lookout for Metrics<a name="services-sns"></a>

You can use Amazon SNS as a channel for anomaly alerts from a Amazon Lookout for Metrics detector\. With Amazon SNS, you can create a topic that has subscribers that use email, SMS, and mobile applications, or applications that use HTTP endpoints, Amazon Simple Queue Service \(Amazon SQS\) queues, or Lambda functions\.

If you don't have an Amazon SNS topic, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) in the Amazon Simple Notification Service Developer Guide\.

With a Lambda function subscriber, you can send anomaly alerts to a webhook or HTTP endpoint that you create in a third party service\. Lookout for Metrics supports the following application channels with Amazon SNS:

****
+ **PagerDuty**
+ **Slack**
+ **Datadog**

**To create an Amazon SNS alert**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Add alert**\.

1. Choose Amazon SNS\.

**Note**  
When you add an Amazon SNS alert to your detector, the Lookout for Metrics console creates a [service role](permissions-service.md) with permission to send notifications to an Amazon SNS topic\.

When your detector finds an anomaly with a severity score that meets or exceeds the alert's threshold, it sends a notification to your Amazon SNS topic with an message that contains details about the anomaly\. 

**Topics**
+ [Using Webhooks](#services-sns-webhooks)
+ [Using Datadog](#services-sns-datadog)
+ [Using Slack](#services-sns-slack)
+ [Using PagerDuty](#services-sns-pagerduty)

## Using Webhooks<a name="services-sns-webhooks"></a>

With an Amazon SNS topic, you can create subscribers that use a webhook in a cloud application\. A webhook is an HTTP endpoint that you call to use some functionality of an application\. The application can be one that you run in your account, or a third party service\.

Amazon SNS has two types of subscriber that you can use with webhooks: Lambda functions and HTTP endpoints\. With an HTTP endpoint, Amazon SNS posts a notification document to the endpoint\. If the webhook supports Amazon SNS notifications as an input, or doesn't use an input, use an HTTP endpoint subscriber\.

If the webhook requires data to be formatted in a specific way, you can use a Lambda function to process anomaly alerts and send a properly formatted document to the webhook\. For example, [Slack](#services-sns-slack) webhooks require a document with a `text` field that contains text to post to the webhook's Slack channel\. You can use a Lambda function to get relevant text from the Amazon SNS notification, format it, and send it to the webhook\.

## Using Datadog<a name="services-sns-datadog"></a>

Datadog provides an HTTP endpoint that you can subscribe to an Amazon SNS topic\. To send anomaly alerts to Datadog, enable AWS integration in your Datadog account and then create a subscription on your Amazon SNS topic with the following settings:

****
+ **Protocol** – HTTPS
+ **Endpoint** –

  `https://app.datadoghq.com/intake/webhook/sns?api_key=YOUR_API_KEY` \(US\)

  Or

  `https://app.datadoghq.eu/intake/webhook/sns?api_key=YOUR_API_KEY` \(EU\)

For more information, see [Amazon SNS](https://docs.datadoghq.com/integrations/amazon_sns/) at [docs\.datadoghq\.com](https://docs.datadoghq.com/)

## Using Slack<a name="services-sns-slack"></a>

With Slack, you can create a webhook that posts a message to a channel\. To format the message into a document that Slack can process, you use a Lambda function subscriber with code that reformats the message into a document with a `text` key\. You can then send the document to the Slack webhook with an HTTP client\.

For instructions on creating the Lambda function, see the following article: [How do I use webhooks to publish Amazon SNS messages to Amazon Chime, Slack, or Microsoft Teams?](https://aws.amazon.com/premiumsupport/knowledge-center/sns-lambda-webhooks-chime-slack-teams/)\.

For details on creating a webhook in Slack, see [Sending messages using Incoming Webhooks ](https://api.slack.com/messaging/webhooks#getting_started) at [api\.slack\.com](https://api.slack.com/)\.

## Using PagerDuty<a name="services-sns-pagerduty"></a>

With PagerDuty, you can create a webhook that triggers an incident with a service integration and the Events API\.

To send anomaly alerts to PagerDuty, create a subscription on your Amazon SNS topic with the following settings:

****
+ **Protocol** – HTTPS
+ **Endpoint** – `https://events.pagerduty.com/integration/INTEGRATION_KEY/enqueue`

For details on creating an integration in PagerDuty, see [Services and Integrations ](https://support.pagerduty.com/docs/services-and-integrations) at [support\.pagerduty\.com](https://support.pagerduty.com/)\.