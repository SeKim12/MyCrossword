#!/bin/bash
set -Eeuo pipefail
trap cleanup SIGINT SIGTERM ERR

cleanup() {
  trap - SIGINT SIGTERM ERR
  docker-compose -f ./docker/docker-compose.yml down -v
  rm -rf ./docker/data
}

# start containers with clean database
while getopts 'r' flag; do
  echo Initiating clean restart, removing existing database...
  case $flag in
    r) rm -rf ./docker/data
       sleep 5 ;;
    *) echo invalid flag, supply -r for clean restart
       exit 1
  esac
done

docker-compose -f ./docker/docker-compose.yml up -d