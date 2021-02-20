#!/bin/bash

echo "Overall Migration Start"
python3 manage.py makemigrations
python3 manage.py migrate

echo "Blog Migration Start"
python3 manage.py makemigrations blog
python3 manage.py migrate

