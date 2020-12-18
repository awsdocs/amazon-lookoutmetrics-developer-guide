# Managing a dataset in Amazon S3<a name="detectors-dataset"></a>

You can use Amazon Simple Storage Service \(Amazon S3\) to store data for an Amazon Lookout for Metrics detector\. With Amazon S3, you have complete control over your data's format and content\. You can preprocess your data before handing it off to Lookout for Metrics, and aggregate data from multiple sources\.

**Note**  
For information about using other AWS services as a datasource, see [Using Amazon Lookout for Metrics with other services](chapter-services.md)\.

You can provide two types of data to a detector: *continuous data* and *historical data*\. A detector monitors continuous data to identify anomalies\. You write continuous data to Amazon S3 as it is generated, to a path that represents the current interval\. At the end of each interval, the detector reads data from the interval and analyzes it\. The following example shows one possible path structure for continuous data with a 5\-minute interval\.

```
s3://my-lookoutmetrics-dataset-123456789012/
    continuous/20201225/1520/data.jsonl
    continuous/20201225/1525/data.jsonl
    continuous/20201225/1530/data.jsonl
```

In this example, data for each 5\-minute interval is stored in a single file named `data.jsonl` at a path that represents the interval\. `continuous/20201225/1520/` is a path for data generated in the 5\-minute period ending at 3:20 PM on December 25th, 2020\. Every 5 minutes, a new path is used\.

Historical data is a collection of data stored at a single path in Amazon S3 that represents many previous intervals\. You can provide historical data to a detector to train it prior to processing continuous data\. Historical data should collect metrics from hundreds or thousands of intervals in one or more files\. The following example shows historical data in separate files for each month at the path `historical/`\.

```
s3://my-lookoutmetrics-dataset-123456789012/
    historical/data-202009.jsonl
    historical/data-202010.jsonl
    historical/data-202011.jsonl
```

**Topics**
+ [Structuring continuous and historical data](#detectors-dataset-livedata)
+ [CSV data](#detectors-dataset-csv)
+ [JSON lines](#detectors-dataset-json)
+ [Providing historical data](#detectors-dataset-learning)
+ [Path template keys](#detectors-dataset-pathkeys)

## Structuring continuous and historical data<a name="detectors-dataset-livedata"></a>

When you choose Amazon S3 as a data source, you provide a *path template* that tells the detector where to find the continuous data\. Consider the following example path structure\.

```
s3://my-lookoutmetrics-dataset-123456789012/
    continuous/20201225/1520/
    continuous/20201225/1525/
    continuous/20201225/1530/
    historical/
```

For historical data for this example, the path is `s3://my-lookoutmetrics-dataset-123456789012/historical`\. Lookout for Metrics looks for data files directly under `historical` and ignores subpaths\.

For continuous data, the detector needs to know where to look for data for the current interval\. The path template for the example structure is `s3://my-lookoutmetrics-dataset-123456789012/continuous/{{yyyyMMdd}}/{{HHmm}}`\. The letters in double brackets represent parts of the path that change depending on the date and time\.

**Date and time keys**
+ `yyyy` – The 4\-digit year
+ `MM` – The 2\- digit month
+ `HH` – The 2\-digit hour \(in 24\-hour format\)
+ `mm` – The 2\-digit minute

For a complete list of supported keys, see [Path template keys](#detectors-dataset-pathkeys)\.

Within a path for a single interval, data can be stored in one tor more text files\. Amazon Lookout for Metrics uses only data with timestamps that fall within the interval for analysis\. The detector uses the dataset's timezone to determine if data belongs to the current interval and ignores data that falls outside of the expected range\.

## CSV data<a name="detectors-dataset-csv"></a>

The following is an example of a correctly formatted CSV input file\. Notice that this sample includes headers for each parameter \(`target_value` is a metric and `item_id` is a dimension\)\. Headers are optional, but recommended\.

```
item_id,timestamp,target_value
item_001,2020-05-07,1591.702780
item_002,2020-05-07,2342.481244
item_003,2020-05-07,1794.275162
item_004,2020-05-07,2716.692446
...
```

The following is an example of a correctly formatted CSV file with headers\. Here, there are two measures \(`target_1` and `target_2`\) and two dimensions \(`item_id` and `store_id`\)\.

```
item_id,store_id,timestamp,target_1,target_2
item_001,store_001,2020-04-01 00:00:00,2117.0433697865165,27.521563807224712
item_002,store_002,2020-04-01 00:00:00,2221.312595828157,28.87706374576604
item_002,store_001,2020-04-01 00:00:00,4224.364287792719,54.91673574130534
item_003,store_002,2020-04-01 00:00:00,1420.3210031715096,18.464173041229625
item_001,store_002,2020-04-01 00:00:00,3222.8693491500876,41.89730153895114
...
```

## JSON lines<a name="detectors-dataset-json"></a>

The following is an example of a correctly formatted JSON lines input file, with `target_value` as a metric and `item_id` as a dimension\.

```
{ "item_id":"item_001" , "timestamp" : "2020-05-07", "target_value" : 1591.702780 }
{ "item_id":"item_002" , "timestamp" : "2020-05-07", "target_value" : 2342.481244 }
{ "item_id":"item_003" , "timestamp" : "2020-05-07", "target_value" : 1794.275162 }
{ "item_id":"item_004" , "timestamp" : "2020-05-07", "target_value" : 2716.692446 }
...
```

The following is another example of a correctly formatted JSON lines file\. Here, `target1` and `target2` are metrics and `item_id` and `store_id` are dimensions\.

```
{"item_id": "item_001", "store_id": "store_001", "timestamp": "2020-04-01 00:00:00", "target1": 2117.0433697865165, "target2": 27.521563807224712}
{"item_id": "item_002", "store_id": "store_002", "timestamp": "2020-04-01 00:00:00", "target1": 2221.312595828157, "target2": 28.87706374576604}
{"item_id": "item_002", "store_id": "store_001", "timestamp": "2020-04-01 00:00:00", "target1": 4224.364287792719, "target2": 54.91673574130534}
{"item_id": "item_003", "store_id": "store_002", "timestamp": "2020-04-01 00:00:00", "target1": 1420.3210031715096, "target2": 18.464173041229625}
{"item_id": "item_001", "store_id": "store_002", "timestamp": "2020-04-01 00:00:00", "target1": 3222.8693491500876, "target2": 41.89730153895114}
...
```

## Providing historical data<a name="detectors-dataset-learning"></a>

Lookout for Metrics stores the continuous data that your detector processes and uses it for learning\. *Learning* is the process of analyzing data over multiple intervals to identify patterns and to distinguish between legitimate anomalies and uncommon but expected variations\. A detector can also learn by using *historical data*\.

To train a detector before it starts processing continuous data, you can provide historical data that represents up to 2,500 previous intervals\. Historical data must fall within a timeframe that varies depending on the dataset's interval\.
+ 5\-minute interval – 3 months
+ 10\-minute interval – 6 months
+ 1\-hour interval – 3 years
+ 1\-day interval – 5 years

If you don't specify a path for historical data when you create the dataset, the detector looks for data from previous intervals in the continuous data path\.

## Path template keys<a name="detectors-dataset-pathkeys"></a>

The following table lists the supported keys for path templates\.


****  

|  Letter  |  Date or time component  |  Presentation  |  Examples  | 
| --- | --- | --- | --- | 
|  y  |  Year  |  Year  |  1996; 96  | 
|  Y  |  Week year  |  Year  |  2009; 09  | 
|  M  |  Month in year  |  Month  |  July;Jul;07  | 
|  d  |  Day in month  |  Number  |  10  | 
|  a  |  AM/PM marker  |  Text  |  PM  | 
|  H  |  Hour in day \(0\-23\)  |  Number  |  0  | 
|  k  |  Hour in day \(1\-24\)  |  Number  |  24  | 
|  k  |  Hour in AM/PM \(0\-11\)  |  Number  |  11  | 
|  m  |  Minute in hour  |  Number  |  30  | 
|  s  |  Second in minute  |  Number  |  55  | 

**Example path structure – daily interval**  
For this example, the path template is s3://my\-lookoutmetrics\-dataset\-123456789012/continuous/\{\{yyyy\}\}/\{\{MM\}\}/\{\{dd\}\}  

```
s3://my-lookoutmetrics-dataset-123456789012/
    historical/
      2020Q2.csv
      2020Q3.csv
    continuous/
      2020/12/01/
        20201201-01.csv
      2020/12/02/
        20201202-01.csv
        20201202-02.csv
```