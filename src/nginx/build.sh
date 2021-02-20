#!/bin/bash

export PROJECT_NAME=mysite

mkdir static media
cp -r /var/www/${PROJECT_NAME}/static/* static
cp -r /var/www/${PROJECT_NAME}/media/* media

docker build -t opeco17/django-template/nginx .

rm -r static
rm -r media