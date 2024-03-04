sudo docker container stop ceramic-container-testing-v2
sudo docker container rm ceramic-container-testing-v2
sudo docker image rm ceramic-img-v2:2024
sudo docker build . -t ceramic-img-v2:2024
sudo docker run -it -d -p 2304:8000 --name ceramic-container-testing-v2 --mount type=bind,source="$(pwd)",target=/ceramic ceramic-img-v2:2024
