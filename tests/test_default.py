import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_svc(host, svc):
    service = host.service("cowrie")
    assert service.is_running
    assert service.is_enabled


def test_cowrie_ssh_listen(host):
    socket = host.socket('tcp://0.0.0.0:2222')
    assert socket.is_listening


def test_cowrie_telnet_listen(host):
    socket = host.socket('tcp://0.0.0.0:2223')
    assert socket.is_listening


def test_cowrie_connection(host):
    command = """echo test | nc root@localhost 2222"""
    cmd = host.run(command)
    assert 'Protocol mismatch' in cmd.stdout
