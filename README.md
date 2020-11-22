# mqttproxy-docker

A container with SSH allowed to one user, without shell access

Password is changed every 30 seconds, brure-force guessing is banned

Use docker-compose to set:
* SSH port
* Password change interval (seconds)
* Maximum failed attempts
* Interval to search for failed attempts (fail2ban syntax)
* Ban time (fail2ban syntax) 


Prebuilt image available at [niksaysit/mqttproxy](https://hub.docker.com/repository/docker/niksaysit/mqttproxy)
