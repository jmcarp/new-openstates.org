#!/bin/sh 

sudo apt install -y python-pip
ansible --version || sudo pip install ansible
