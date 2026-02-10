#!/bin/bash
set -e

APP_NAME="acs-simple"
IMAGE="acs-simple:staging"
CONTAINER="${APP_NAME}-staging"
PORT="8091"

echo "🚀 Deploying STAGING..."

docker rm -f $CONTAINER || true

docker run -d \
  --name $CONTAINER \
  -p ${PORT}:3000 \
  $IMAGE

echo "✅ STAGING deployed at http://<server-ip>:${PORT}"
