#!/bin/bash

docker-compose down

sleep 2

docker-compose up -d --build

sleep 3

python script.py

xdg-open http://localhost:8000/docs
