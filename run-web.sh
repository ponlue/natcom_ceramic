
sudo docker container stop ceramic-container-testing
sudo docker container rm ceramic-container-testing
sudo docker image rm ceramic-img-testing:2024
sudo docker build -t ceramic-img-testing:2024 .
sudo docker run -it -d -p 9999:9999 --name ceramic-container-testing --mount type=bind,source="$(pwd)",target=/ceramic ceramic-img-testing:2024
