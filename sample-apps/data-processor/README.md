# Amazon Lookout for Metrics data processor

This sample application reads events from AWS CloudTrail, converts them into timeseries format, and stores them in Amazon S3 for use with Amazon Lookout for Metrics. Lookout for Metrics requires data to be formatted as a series of timestamped records and stored in a directory that indicates when it was gathered. The sample application can run locally to generate data on demand, or run on a schedule in AWS Lambda to generate data continuously.

![Architecture](images/sample-data-processor.png)

The project source includes function code and supporting resources:

- `function` - A Python function.
- `template.yml` - An AWS CloudFormation template that creates an application.
- `1-create-bucket.sh`, `2-build-layer.sh`, etc. - Shell scripts that use the AWS CLI to deploy and manage the application.

Use the following instructions to deploy the sample application.

# Requirements
- [Python 3.7](https://www.python.org/downloads/)
- The Bash shell. For Linux and macOS, this is included by default. In Windows 10, you can install the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to get a Windows-integrated version of Ubuntu and Bash.
- [The AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) v1.17 or newer.

If you use the AWS CLI v2, add the following to your [configuration file](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) (`~/.aws/config`):

```
cli_binary_format=raw-in-base64-out
```

This setting enables the AWS CLI v2 to load JSON events from a file, matching the v1 behavior.

# Setup
Download or clone this repository.

    $ git clone https://github.com/awsdocs/amazon-lookoutmetrics-developer-guide.git
    $ cd amazon-lookoutmetrics-developer-guide/sample-apps/data-processor

To create a new bucket for deployment artifacts, run `1-create-bucket.sh`.

    data-processor$ ./1-create-bucket.sh
    make_bucket: lookoutmetrics-dataset-a5e491dbb5b22e0d

To build a Lambda layer that contains the function's runtime dependencies, run `2-build-layer.sh`. Packaging dependencies in a layer reduces the size of the deployment package that you upload when you modify your code.

    data-processor$ ./2-build-layer.sh

To run the code locally (optional), install the function's dependencies in a virtual environment. You can use the `pipenv` package to create a virtual environment and install dependencies at the same time.

    data-processor$ pip install pipenv
    data-processor$ pipenv install

By default, the application reads CloudTrail events emitted by AWS KMS for operations such as `Decrypt`. To get events for a different service, change the value of the `SERVICE` variable in `3-deploy.sh` to another name such as `iam` or `lambda`.

# Deploy
To deploy the application, run `3-deploy.sh`.

    data-processor$ ./3-deploy.sh
    Uploading to e678bc216e6a0d510d661ca9ae2fd941  4394 / 4394.0  (100.00%)
    Successfully packaged artifacts and wrote output template to file out.yml.
    Waiting for changeset to be created..
    Waiting for stack create/update to complete
    Successfully created/updated stack - lookoutmetrics-data-processor

This script uses AWS CloudFormation to deploy the Lambda functions and an IAM role. If the AWS CloudFormation stack that contains the resources already exists, the script updates it with any changes to the template or function code.

# Test
To invoke the function, run `4-invoke.sh`.

    data-processor$ ./4-invoke.sh
    {
        "StatusCode": 200,
        "ExecutedVersion": "$LATEST"
    }
    "s3://lookoutmetrics-dataset-a33dxmplff890241/timeseries/20210317/2300/kms-timeseries-20210317-2300.csv"

The test event generates a one-hour interval's worth of data for the most recent full hour and stores it in the application's bucket.

To get the file out of S3, use the `aws s3 cp` command with the URI that the function returns.

    data-processor$ aws s3 cp s3://lookoutmetrics-dataset-a33dxmplff890241/timeseries/20210317/2300/kms-timeseries-20210317-2300.csv .

    $ head kms-timeseries-20210317-2300.csv
    EventTime,EventId,EventSource,EventName,ReadOnly,AccessKeyId,Username,Calls,Date
    2021-03-17 22:00:08+00:00,ededd82d-xmpl-424d-8564-47df3ee1f0bd,kms.amazonaws.com,Decrypt,true,ASIAXMPL7W66TXMPLVJK,lookoutmetrics-sample-function-16GYXMPLO52OR,1,2021-03-17 22:00:08
    2021-03-17 22:00:08+00:00,03b5fc97-xmpl-414a-93eb-0fd1190e18c4,kms.amazonaws.com,Decrypt,true,none,none,1,2021-03-17 22:00:08
    2021-03-17 22:00:08+00:00,32b10683-xmpl-4398-89ef-d65cfecd6f68,kms.amazonaws.com,Decrypt,true,none,none,1,2021-03-17 22:00:08

To run the same code locally with the `unittest` library, run `0-run-tests.sh`

    ## ENVIRONMENT VARIABLES
    {"EDITOR": "vim", "HOME": "/home/...\n"}
    ## EVENT
    {"service": "kms"}
    ## CONTEXT
    {"requestid": "1234"}
    uploading file: timeseries/20210317/2300/kms-timeseries-20210317-2300.csv
    s3://lookoutmetrics-dataset-a33d3c7cff890241/timeseries/20210317/2300/kms-timeseries-20210317-2300.csv
    .
    ----------------------------------------------------------------------
    Ran 1 test in 5.594s

    OK

# Backfill

To generate 2 weeks of historical data, run `5-backfill.sh`.

    data-processor$ ./5-backfill.sh


The application uses AWS X-Ray to trace requests. Open the [X-Ray console](https://console.aws.amazon.com/xray/home#/service-map) to view the service map. The following service map shows the function calling Amazon S3.

![Service Map](images/data-processor-servicemap.png)

Choose a node in the main function graph. Then choose **View traces** to see a list of traces. Choose any trace to view a timeline that breaks down the work done by the function.

![Trace](images/data-processor-trace.png)

# Cleanup

To deactivate a virtual environment, run `deactivate`.

    (data-processor) data-processor$ deactivate

To delete the application, run `6-cleanup.sh`.

    data-processor$ ./6-cleanup.sh

To delete the pipenv virtual environment, run `pipenv --rm`.

    data-processor$ pipenv --rm

If you ran the application locally, you can also delete the files that it generated in `/tmp`.

    $ rm -r /tmp/*timeseries*.csv
