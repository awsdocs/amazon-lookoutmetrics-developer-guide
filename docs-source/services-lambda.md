# Using AWS Lambda with Lookout for Metrics<a name="services-lambda"></a>

You can use AWS Lambda as a channel for anomaly alerts from an Amazon Lookout for Metrics detector\. With a Lambda function, you can process anomaly alerts in your preferred programming language, and use the AWS SDK to interact with other AWS services\.

Lambda is a serverless way for you to run code in AWS\. Your code only runs and only incurs charges when it is invoked\. If you don't already have a Lambda function, see [Create a Lambda function with the console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html) in the Lambda Developer Guide to get started\.

**To create a Lambda alert**

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com//lookoutmetrics/home#detectors) page\.

1. Choose a detector\.

1. Choose **Add alert**\.

1. Choose **AWS Lambda**\.

1. Choose a function\.

**Note**  
When you add a Lambda alert to your detector, the Lookout for Metrics console creates a [service role](permissions-service.md) with permission to invoke the function\.

When your detector finds an anomaly with a severity score that meets or exceeds the alert's threshold, it invokes your Lambda function with an event that contains details about the anomaly\. The Lambda runtime converts this document into an object and passes it to your function's *handler method*\. You can use this object to perform additional processing, to record details about the anomaly in a database or storage, or to call another service\.

For sample code in all programming languages supported by Lambda, see [Lambda sample applications](https://docs.aws.amazon.com/lambda/latest/dg/lambda-samples.html) in the AWS Lambda Developer Guide\.