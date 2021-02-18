#!/bin/bash

kubectl apply -f manifests/general-config.yaml
kubectl apply -f manifests/database-secret.yaml

sleep 5

kubectl apply -f manifests/database.yaml

sleep 30