Ansible-Cowrie
##############

Ansible scripts for Cowrie

Requirements
============

* User with SUDO 

Usage
============

Edit sites.yaml and replace $USER with appropriate user. Needs sudo access

Overview
============

Config values are located in roles/cowrie/defaults/main.yaml

* Update, install packages & pip install 

* Set up Cowrie users with home directory located in /opt/cowrie.

* Clone https://github.com/cowrie/cowrie into /opt/cowrie/cowrie

* Setup virtual environment in /opt/cowrie-env for honeypot & install packages 

* Start Cowrie port 2222
