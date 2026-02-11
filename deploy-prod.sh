#!/bin/bash
set -e

CONTAINER_NAME="acs-simple-prod"
IMAGE_NAME="acs-simple:main"
PORT="8090"
APP_ENV="production"

echo "Stopping old container (if exists)..."
docker rm -f ${CONTAINER_NAME} || true

echo "Starting production container..."
docker run -d \
  --name ${CONTAINER_NAME} \
  -p ${PORT}:3000 \
  ${IMAGE_NAME}

echo "Production deploy SUCCESS"
