#!/usr/bin/env bash

set -e
cd $(pwd)/docker
docker-compose --file docker-compose.base.yml up --remove-orphans