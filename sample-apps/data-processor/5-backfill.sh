#!/bin/bash
set -eo pipefail
BUCKET=$(cat bucket-name.txt)
python3 function/lambda_function.test.py TestFunction.test_backfill
mkdir -p /tmp/backfill
mv /tmp/kms-timeseries* /tmp/backfill
aws s3 sync /tmp/backfill s3://$BUCKET/backtest/