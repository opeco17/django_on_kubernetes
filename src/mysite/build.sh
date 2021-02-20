#!/bin/bash

cd mysite
python3 manage.py collectstatic --no-input
cd ..

docker build -t opeco17/django-template/mysite .