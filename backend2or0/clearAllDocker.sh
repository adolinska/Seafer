#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Nadaj uprawnienia Hauptmana [SUDO]"
  exit
fi

sudo docker kill $(sudo docker ps -q)
sudo docker rm $(sudo docker ps -a -q) 
sudo docker volume rm $(sudo docker volume ls -q)
sudo docker system prune
