#!/bin/bash
# sudo rm -rf web
# sudo mkdir web
# sudo cp -r ceramic web
# sudo cp -r home web
# sudo cp manage.py web
# sudo cp -r static web
# sudo chown natcom:natcom_sothatna -R web

sudo docker container stop sothatna-webapp-container
sudo docker container rm sothatna-webapp-container
sudo docker image rm sothatna-img-app:2024
sudo docker build . -t="sothatna-img-app:2024"
sudo docker run -it -d -p 5063:8000 --name sothatna-webapp-container --mount type=bind,source="$(pwd)/web/",target=/web sothatna-img-app:2024