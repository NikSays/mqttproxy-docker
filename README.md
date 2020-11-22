# mqttproxy-docker

A container with SSH allowed to one user, without shell access

Password is changed every 30 seconds, brure-force guessing is banned

Use docker-compose to set:
* SSH port
* Password change interval (seconds)
* Maximum failed attempts
* Interval to search for failed attempts (fail2ban syntax)
* Ban time (fail2ban syntax)

### Prebuilt image

Prebuilt image available at [niksaysit/mqttproxy](https://hub.docker.com/repository/docker/niksaysit/mqttproxy)

docker-compose.yml to use with prebuilt image
```
version: "3.9"
services:
  ssh:
    image: niksaysit/mqttproxy
    ports:
      - "22:22"
    environment:
      INTERVAL: 30
      BAN_ATTEMPTS: 5
      BAN_TIME: 12h
      BAN_FIND_INTERVAL: 10m
    cap_add:
      - NET_ADMIN
    volumes:
      - "./keys/:/opt/keys/"
