# Create a datasource in Amazon S3<a name="gettingstarted-datasource"></a>

To get started with Lookout for Metrics, create a dataset that you can look for anomalies in\. You can use data that you already have, or generate data with a sample application\.

A Lookout for Metrics detector can read data in an Amazon S3 bucket in CSV or JSON lines format\. Each record must have a numerical field to monitor \(a *measure*\) and a field that represents a date or timestamp\. Records can also have categorical fields \(*dimensions*\), additional measures, and fields that are not monitored\.

For example, the following example is a CSV file that has a measure field named `Calls`, a timestamp field named `Date`, and text fields that could be used as dimensions\.

**Example CSV file**  

```
Date,EventSource,EventName,ReadOnly,AccessKeyId,Username,Calls
2021-03-12 22:00:07,kms.amazonaws.com,GenerateDataKey,true,none,none,1
2021-03-12 22:00:12,kms.amazonaws.com,Decrypt,true,ASIAXMPLV4CQYXGMLRQ,greg,1
2021-03-12 22:00:36,kms.amazonaws.com,Decrypt,true,ASIAXMPLVMP6KEG3BRA,michael,1
```

In the example, there is a header row with names for each field, fields are separated by commas, and values are not enclosed in quotes\. The header is optional, but it simplilfies configuration\. Values can be enclosed in single or double quotes\. In addition to commas, tabs, spaces, and pipes \(`|`\) can be used as delimeters\.

**Topics**
+ [Collect existing data](#gettingstarted-datasource-backtest)
+ [Generate data with a sample application](#gettingstarted-datasource-generate)
+ [Download sample data](#gettingstarted-datasource-download)

## Collect existing data<a name="gettingstarted-datasource-backtest"></a>

To use existing data to run a backtest, collect it in one or more files and store it in a single folder in an Amazon S3 bucket\. The data must contain timestamped entries for at least 285 intervals, where an interval is 5 minutes, 10 minutes, 1 hour, or 1 day long\. Each file can have entries for one interval or multiple intervals\.

```
s3://lookoutmetrics-dataset-1234567891012/backtest/20210104-20210110.csv
                                                   20210111-20210117.csv
                                                   20210118-20210125.csv
```

To use a detector in continuous mode, you need to store it at a different path for each interval as the intervals occur\. For an example of how to do this, [run the sample application](#gettingstarted-datasource-generate)\.

For more information about supported data formats and folder structures, see [Managing a dataset in Amazon S3](detectors-dataset.md)\.

## Generate data with a sample application<a name="gettingstarted-datasource-generate"></a>

The GitHub repository for this guide includes a sample application that you can use to generate a dataset with data from your AWS account\. The sample application runs locally or in AWS Lambda\. It uses the AWS SDK to read events from AWS CloudTrail, reformats them with Pandas, and stores them in Amazon S3\.

**Example [lambda\_function\.py](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-apps/data-processor/function/lambda_function.py) – Processing data**  

```
...
def process_events(end_time, service):
    start_time = end_time - timedelta(minutes=60)
    records = []
    # call CloudTrail
    responses = get_events(service, start_time, end_time)
    records = [{k: event.get(k) for k in fields} for response in responses for event in response.get('Events')]
    # format timeseries dataframe
    df = pd.DataFrame(records)
    ...
```

To set up the application, follow the instructions [in the README file](https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide/blob/main/sample-apps/data-processor)\. To generate a dataset for a backtest, run the backfill script\.

```
(data-processor) data-processor$ ./5-backfill.sh
```

In Lambda, the application runs once every hour to generate a timeseries for the previous hour\. The backfill script runs the application locally to generate two weeks worth of data and store it in the application's S3 bucket\.

## Download sample data<a name="gettingstarted-datasource-download"></a>

Sample data is available in the service's GitHub repository at [github\.com/aws\-samples/amazon\-lookout\-for\-metrics\-samples](https://github.com/aws-samples/amazon-lookout-for-metrics-samples)\. The samples repository provides an archive of sample data and instructions for using it with a detector\.