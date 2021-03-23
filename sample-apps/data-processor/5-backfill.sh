#!/bin/bash
set -eo pipefail
python3 function/lambda_function.test.py TestFunction.test_backfill
