#!/bin/bash
# sudo rm -rf web
# sudo mkdir web
# sudo cp -r ceramic web
# sudo cp -r home web
# sudo cp manage.py web
# sudo cp -r static web
# sudo chown natcom:natcom_sothatna -R web

docker container stop sothatna-webapp-container
docker container rm sothatna-webapp-container
docker image rm sothatna-img-app:2024
docker build . -t="sothatna-img-app:2024"
docker run -it -d -p 5063:8000 --name sothatna-webapp-container --mount type=bind,source="$(pwd)",target=/web sothatna-img-app:2024
