# Nginx configuration example serving a flask server

> This project requires docker/docker-compose to run, please make sure you have it on your machine before running the commands below.
> For more info: [Docker documentation](https://docs.docker.com/).

To be able to check if the round robin is workin, we want to create more than 1 container for our app, so let's run the following command:

`docker compose up -d --scale app=3`

>By running docker compose with the `--scale` flag, we can specify the amount of containers to be created for a service.
>**Tip:** You can check if the containers are up using `docker ps`

With all the containers up and running, you should be able to type `localhost` on your browser and check the round robin working for each refresh you do on the page.


![alt-text](https://cdn.iconscout.com/icon/free/png-256/free-nginx-3521604-2945048.png)![alt-text](https://cdn.iconscout.com/icon/free/png-256/free-flask-51-285137.png?f=webp)![alt-text](https://static.wixstatic.com/media/4bef97_3fca4225935f490783ac9ecb3f27a8b1~mv2.png/v1/fill/w_256,h_256,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/python_logo.png)
