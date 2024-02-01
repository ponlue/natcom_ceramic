#!/bin/bash
sudo docker container stop sothatna-webapp-container
sudo docker container rm sothatna-webapp-container
sudo docker image rm sothatna-img-app:2024
sudo docker build . -t="sothatna-img-app:2024"
sudo docker run -it -d -p 5063:8000 --name sothatna-webapp-container --mount type=bind,source="$(pwd)",target=/web sothatna-img-app:2024
