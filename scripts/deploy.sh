#!/bin/bash

set -e

cd ~/ai-backend-deployment

git fetch origin
git reset --hard origin/main

docker compose up -d --build --remove-orphans

docker image prune -f
