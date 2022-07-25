#!/bin/bash
docker build -t python-docker .
# login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 675115824335.dkr.ecr.us-east-1.amazonaws.com
# tag for ECR
docker tag python-docker:latest 675115824335.dkr.ecr.us-east-1.amazonaws.com/python-docker:latest
# push to ECR
docker push 675115824335.dkr.ecr.us-east-1.amazonaws.com/python-docker:latest

