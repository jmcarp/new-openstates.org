#!/bin/sh 

sudo apt install -y python-pip awscli
credstash -h || sudo pip install credstash
ansible --version || sudo pip install ansible
