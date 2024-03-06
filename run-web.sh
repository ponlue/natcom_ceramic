<<<<<<< HEAD
sudo docker container stop ceramic-container-testing
sudo docker container rm ceramic-container-testing
sudo docker image rm ceramic-img-testing:2024
sudo docker build -t ceramic-img-testing:2024 .
sudo docker run -it -d -p 9999:9999 --name ceramic-container-testing --mount type=bind,source="$(pwd)",target=/web ceramic-img-testing:2024
=======
sudo docker container stop sothatna-ceramic-container
sudo docker container rm sothatna-ceramic-container
sudo docker image rm sothatna-ceramic-img:2024
sudo docker build . -t sothatna-ceramic-img:2024
sudo docker run -it -d -p 5063:8000 --name sothatna-ceramic-container --mount type=bind,source="$(pwd)",target=/ceramic sothatna-ceramic-img:2024
>>>>>>> testing-v1
