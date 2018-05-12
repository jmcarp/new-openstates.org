#!/bin/sh 

sudo apt install -y python-pip
sudo pip install -U pip
ansible --version || sudo pip install ansible
