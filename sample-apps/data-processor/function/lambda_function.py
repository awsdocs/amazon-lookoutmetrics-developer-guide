import os
import logging
import jsonpickle
import boto3
import time
import json
import pandas as pd
from datetime import timedelta
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

# logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# tracing (AWS X-Ray)
patch_all()
# AWS SDK clients
session = boto3.Session()
clout = session.client('cloudtrail')
s3 = boto3.resource('s3')
# globals
ymdhms = '%Y-%m-%d %H:%M:%S'
ymd = '%Y%m%d'
ym = '%Y%m'
hm = '%H%M'
dir = '/tmp'
ct_throttle_sleep = 2
fields = ['EventTime','EventId','EventSource','EventName','ReadOnly','AccessKeyId','Username']

def lambda_handler(event, context):
    """
    Process AWS Lambda events to generate reports.

    :param event: The Lambda invocation payload, a JSON document with parameters.
    :param context: Details about the Lambda runtime environment
    :return: returns the location of a report in Amazon S3
    """
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(jsonpickle.encode(dict(**os.environ)))
    logger.info('## EVENT')
    logger.info(jsonpickle.encode(event))
    logger.info('## CONTEXT')
    logger.info(jsonpickle.encode(context))
    # read parameters from invocation event
    service = event.get('service','kms')
    start_date = pd.to_datetime(event.get('start_date'),utc=True)
    end_date = pd.to_datetime(event.get('end_date'),utc=True)
    backfill = event.get('backfill')
    # backfill: set range to last 2 weeks
    if backfill:
        end_date = pd.Timestamp.utcnow().floor('1H')
        start_date = end_date - timedelta(days=14)
    # process specified date range or backfill range
    if start_date and end_date:
        result = '503 internal error'
        for hour in date_range(start_date, end_date):
            end_time = hour.floor('1H')
            logger.info('Processing {}'.format(end_time))
            result = process_events(end_time, service)
            time.sleep(ct_throttle_sleep)
        return result
    # end_date only: process one specific interval
    if end_date:
        end_time = end_date.floor('1H')
        result = process_events(end_time, service)
        return result
    # default: process most recent interval
    end_time = pd.Timestamp.utcnow().floor('1H')
    result = process_events(end_time, service)
    return result

def process_events(end_time, service):
    start_time = end_time - timedelta(minutes=60)
    records = []
    # call CloudTrail
    responses = get_events(service, start_time, end_time)
    records = [{k: event.get(k) for k in fields} for response in responses for event in response.get('Events')]
    # format timeseries dataframe
    df = pd.DataFrame(records)
    if len(df) == 0:
        return '404 no events found for service {}'.format(service)
    df['EventTime'] = pd.to_datetime(df['EventTime'], utc=True)
    timeseries = df.set_index('EventTime')
    timeseries.sort_index(inplace=True)
    # add measure column
    timeseries['Calls'] = 1
    # save and upload
    now = pd.Timestamp.utcnow()
    report_file = '{}-timeseries-{}.csv'.format(service,now.strftime(ymdhms))
    report_path = '{}/{}'.format(dir,report_file)
    report_key = 'timeseries/{}/{}/{}'.format(start_time.strftime(ymd), start_time.strftime(hm), report_file)
    timeseries['Date'] = timeseries.index.strftime(ymdhms)
    timeseries.fillna('none').to_csv(report_path, index_label='EventTime')
    bucket = os.environ.get('bucket')
    if bucket:
        upload(bucket, report_key, report_path)
        return 's3://{}/{}'.format(bucket,report_key)
    return '200 success'

def get_events(service, start_time, end_time):
    service_att = [{'AttributeKey': 'EventSource','AttributeValue': '{}.amazonaws.com'.format(service)}]
    paginator = clout.get_paginator('lookup_events')
    responses = paginator.paginate(StartTime=start_time,
                                    LookupAttributes=service_att,
                                    EndTime=end_time)
    return responses

def upload(bucket, key, src):
    logger.info('uploading file: {}'.format(key))
    s3.Bucket(bucket).Object(key).upload_file(src)
    return

def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).total_seconds()/3600 + 1)):
        yield pd.to_datetime(start_date + timedelta(hours=n), utc=True)