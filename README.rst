Ansible-Cowrie
##############

This is work in progress, not ready to deploy yet

|travis|_

Ansible role to deploy the Cowrie SSH/Telnet Honeypot.

Requirements
--------------

Currently root access is required to create the appropriate users and modify the Linux firewall.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Config values are located in `defaults/main.yaml`

Example Playbook
----------------

Example::

    - hosts: honeypots
      roles:
         - { role: ansible-cowrie }

.. |travis| image:: https://travis-ci.com/cowrie/ansible-cowrie.svg?branch=master
.. _travis: https://travis-ci.com/cowrie/ansible-cowrie
