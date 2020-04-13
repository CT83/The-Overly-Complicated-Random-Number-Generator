# The-Complicated-Simple-Container-App
[![Build Status](https://travis-ci.org/CT83/The-Complicated-Simple-Container-App.svg?branch=master)](https://travis-ci.org/CT83/The-Complicated-Simple-Container-App)

# Docker Compose 

`docker-compose up --build`

`docker-compose -f docker-compose-prod.yml up --build -d`

# Kubernetes

1. How to start the Client

`kubectl apply -f client-pod.yaml`
`kubectl apply -f client-node-port.yaml`

`kubectl delete -f client-pod.yaml`
`kubectl delete -f client-node-port.yaml`

