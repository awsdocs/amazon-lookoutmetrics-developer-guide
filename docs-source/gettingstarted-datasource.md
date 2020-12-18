# Prepare data files<a name="gettingstarted-datasource"></a>

In this section, you format the data that the detector uses for learning and anomaly detection\.

**Note**  
Sample data is available in the service's GitHub repo at [github\.com/aws\-samples/amazon\-lookout\-for\-metrics\-samples](https://github.com/aws-samples/amazon-lookout-for-metrics-samples)\.

**To prepare your data**

1. Select the data you want to use with Lookout for Metrics\. Records in your data must have a timestamp and a numerical field to monitor \(a measure\)\.

1. Choose an interval\. The detector's interval can be daily, hourly, every ten minutes, or every five minutes\. The interval determines how you organize files in Amazon S3\. 

1. Format your data into JSON lines or CSV\. each line of data is a record that has a timestamp and at least one measure\. Data can be split into multiple files within an interval\.

1. Organize your continuous data in Amazon S3\. The following example shows a folder structure for a five\-minute interval:

   ```
   s3://DOC-EXAMPLE-BUCKET1/
       project1/input/
           live/
               20200401/
                   0000/
                       20200401_0000-0.csv
                   0005/
                       20200401_0005-0.csv 
                       20200401_0005-1.csv
   ```

   Each interval has a separate path, such as `s3://DOC-EXAMPLE-BUCKET1/project1/input/live/20200401/0000/`\.

   The path template for the detector is an Amazon S3 URI with placeholders for the date and time: `s3://DOC-EXAMPLE-BUCKET1/project1/input/live/{{yyyyMMdd}}/{{HHmm}}`\.

1. \(Optional\) Create a data file with historical data for learning or to run a backtest\. This can be one or more files with data from a large number of past intervals\. The files must all be at the same path

   ```
   s3://DOC-EXAMPLE-BUCKET1/
       project1/input/
           historical/
               2020-10.csv
               2020-11.csv
               2020-12.csv
   ```

   The historical data location is an absolute path: `s3://DOC-EXAMPLE-BUCKET1/project1/input/historical`\.