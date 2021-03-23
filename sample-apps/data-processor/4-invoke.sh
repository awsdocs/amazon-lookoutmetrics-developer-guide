#!/bin/bash
set -eo pipefail
STACK_NAME=lookoutmetrics-data-processor
FUNCTION=$(aws cloudformation describe-stack-resource --stack-name $STACK_NAME --logical-resource-id function --query 'StackResourceDetail.PhysicalResourceId' --output text)

aws lambda invoke --function-name $FUNCTION --payload file://event.json out.json
cat out.json
echo ""