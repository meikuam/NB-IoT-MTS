# NB-IoT-MTS


## change configs:

```shell
cp config.json.dist config.json
cp docker/.env.dist docker/.env
```

## install docker and docker-compose (using Ubuntu 18.04)

```shell
# install docker
sudo apt install ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
sudo apt update
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo usermod -aG docker $USER

# install docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.0.1/docker-compose-linux-aarch64" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## run docker-compose:

```shell
cd docker && docker-compose up -d 
```

## see results on web:

![gigachad](images/example_web.png)

## example logs from CoAP:

![gigachad](images/example_coap.png)


## Да, я слышал про контейнеры. Не думал что разработчики работают в порту.
![gigachad](images/gigachad.jpg)