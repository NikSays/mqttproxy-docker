# mqttproxy-docker

A container with SSH allowed to one user, without shell access, with tor gateway

Password is changed every 30 seconds, brure-force guessing is banned

Use docker-compose to set:
* SSH port
* Password change interval (seconds)
* Maximum failed attempts
* Interval to search for failed attempts (fail2ban syntax)
* Ban time (fail2ban syntax)

### Connecting
#### SOCKS
`ssh user@{{ip}} -p 2022 -ND {{local SOCKS port}} -L 853:localhost:853`
then, use `localhost:{{local SOCKS port}}` as your proxy, and localhost as your dns
#### TOR
`ssh user@{{ip}} -p 2022 -NL {{local TOR port}}:localhost:9150`
then, use `localhost:{{local TOR port}}` as your proxy

### Prebuilt image

Prebuilt image available at [niksaysit/mqttproxy](https://hub.docker.com/r/niksaysit/mqttproxy)

####docker-compose.yml to use with prebuilt image
```
version: "3.9"
services:
  ssh:
    image: niksaysit/mqttproxy
    ports:
      - "2022:22"
    environment:
      INTERVAL: 30
      BAN_ATTEMPTS: 5
      BAN_TIME: 12h
      BAN_FIND_INTERVAL: 10m
    cap_add:
      - NET_ADMIN
    volumes:
      - "./keys/:/opt/keys/"     
      - "./ag/work/:/opt/adguardhome/work/"
      - "./ag/conf/:/opt/adguardhome/conf/"
```
####Also docker command 
```
docker run --rm \
-p 2022:22 \
-v $FOLDER/keys/:/opt/keys/ \
-v $FOLDER/ag/work/:/opt/adguardhome/work/ \
-v $FOLDER/ag/conf/:/opt/adguardhome/conf/ \
--env-file ./env \
--cap-add=NET_ADMIN \
niksaysit/mqttproxy
```
env file:
```
INTERVAL=30
BAN_ATTEMPTS=5
BAN_TIME=12h
BAN_FIND_INTERVAL=10m
```
