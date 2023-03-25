#!/bin/bash
sudo docker stop $(sudo docker ps -a -q)

sudo docker rm -vf $(sudo docker ps -aq)

sudo docker rmi -f $(sudo docker images -aq)
