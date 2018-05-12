#!/bin/sh

cd /tmp/cd-new-openstates.org/
ansible-playbook -i inventory/ openstates.yml
