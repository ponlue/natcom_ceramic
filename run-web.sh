#!/bin/bash
# sudo rm -rf web
# sudo mkdir web
# sudo cp -r ceramic web
# sudo cp -r home web
# sudo cp manage.py web
# sudo cp -r static web
# sudo chown natcom:natcom_sothatna -R web

docker container stop meng-webapp-container
docker container rm meng-webapp-container
docker image rm meng-img-app:2024
docker build . -t="meng-img-app:2024"
docker run -it -d -p 5555:8000 --name meng-webapp-container --mount type=bind,source="$(pwd)",target=/web meng-img-app:2024
