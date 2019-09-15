import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


CHROME_BINARY_PATH = '/usr/bin/google-chrome'
CHROME_PACKAGE = 'google-chrome-stable'
CHROME_DEBIAN_REPO = '/etc/apt/sources.list.d/google-chrome.list'
CHROME_EL_REPO = '/etc/yum.repos.d/google-chrome.repo'


def test_googlechrome_package_installed(host):
    host.package("CHROME_PACKAGE").is_installed


def test_googlechrome_binary_exists(host):
    host.file('CHROME_BINARY_PATH').exists


def test_googlechrome_binary_symlink(host):
    host.file('CHROME_BINARY_PATH').is_symlink


def test_googlechrome_binary_which(host):
    host.check_output('which google-chrome') == CHROME_BINARY_PATH


def test_atom_repo_exists(host):
    host.file('CHROME_DEBIAN_REPO').exists or \
      host.file('CHROME_EL_REPO').exists


def test_atom_repo_file(host):
    host.file('CHROME_DEBIAN_REPO').is_file or \
      host.file('CHROME_EL_REPO').is_file
