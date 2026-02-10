#!/bin/bash
set -e

APP="acs-simple-"
PORT="8090"

docker rm -f ${APP}-prod || true
docker run -d \
  --restart always \
  --name ${APP}-prod \
  -p ${PORT}:3000 \
  ${APP}:main
