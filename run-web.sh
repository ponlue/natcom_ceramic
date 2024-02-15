sudo docker container stop sothatna-ceramic-container
sudo docker container rm sothatna-ceramic-container
sudo docker image rm sothatna-ceramic-img:2024
sudo docker build . -t sothatna-ceramic-img:2024
sudo docker run -it -d -p 5063:8000 --name sothatna-ceramic-container --mount type=bind,source="$(pwd)",target=/web sothatna-ceramic-img:2024
