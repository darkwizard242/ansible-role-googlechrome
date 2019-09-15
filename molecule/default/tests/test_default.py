import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


CHROME_BINARY_PATH = '/usr/bin/google-chrome'
CHROME_PACKAGE = 'google-chrome-stable'


def test_googlechrome_package_installed(host):
    host.package("CHROME_PACKAGE").is_installed


def test_googlechrome_binary_exists(host):
    host.file('CHROME_BINARY_PATH').exists


def test_googlechrome_binary_symlink(host):
    host.file('CHROME_BINARY_PATH').is_symlink


def test_googlechrome_binary_which(host):
    host.check_output('which google-chrome') == CHROME_BINARY_PATH
