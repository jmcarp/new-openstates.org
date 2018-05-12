#!/bin/sh

cd /tmp/cd-new-openstates.org/deployment/
ansible-playbook -i inventory/ openstates.yml
