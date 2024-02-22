sudo docker container stop sothatna-ceramic-container-testing
sudo docker container rm sothatna-ceramic-container-testing
sudo docker image rm sothatna-ceramic-img-testing:2024
sudo docker build . -t sothatna-ceramic-img-testing:2024
sudo docker run -it -d -p 5063:8000 --name sothatna-ceramic-container-testing --mount type=bind,source="$(pwd)",target=/web sothatna-ceramic-img-testing:2024
