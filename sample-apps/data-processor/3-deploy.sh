#!/bin/bash
set -eo pipefail
STACK_NAME=lookoutmetrics-data-processor
ARTIFACT_BUCKET=$(cat bucket-name.txt)
SERVICE=kms
aws cloudformation package --template-file template.yml --s3-bucket $ARTIFACT_BUCKET --output-template-file out.yml
aws cloudformation deploy --template-file out.yml --stack-name $STACK_NAME --capabilities CAPABILITY_NAMED_IAM --parameter-overrides bucketName=$ARTIFACT_BUCKET serviceName=$SERVICE
