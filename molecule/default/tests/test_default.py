import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_googlechrome_package_installed(host):
    assert host.package("google-chrome-stable").is_installed


def test_googlechrome_binary_exists(host):
    assert host.file('/usr/bin/google-chrome').exists


def test_googlechrome_binary_symlink(host):
    assert host.file('/usr/bin/google-chrome').is_symlink


def test_googlechrome_binary_which(host):
    assert host.check_output('which google-chrome') == '/usr/bin/google-chrome'


def test_atom_repo_exists(host):
    assert host.file('/etc/apt/sources.list.d/google-chrome.list').exists or \
      host.file('/etc/yum.repos.d/google-chrome.repo').exists


def test_atom_repo_file(host):
    assert host.file('/etc/apt/sources.list.d/google-chrome.list').is_file or \
      host.file('/etc/yum.repos.d/google-chrome.repo').is_file
