#!/bin/bash
set -e

APP="acs-simple"
PORT="8091"

docker rm -f ${APP}-staging || true
docker run -d \
  --name ${APP}-staging \
  -p ${PORT}:3000 \
  ${APP}:staging
