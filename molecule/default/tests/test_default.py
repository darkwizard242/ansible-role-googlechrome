import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'google-chrome-stable'
PACKAGE_BINARY = '/usr/bin/google-chrome'
DEBIAN_REPO_FILE = '/etc/apt/sources.list.d/google-chrome.list'
EL_REPO_FILE = '/etc/yum.repos.d/google-chrome.repo'


def test_googlechrome_package_installed(host):
    """
    Tests if google-chrome-stable packages is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_googlechrome_binary_exists(host):
    """
    Tests if google-chrome binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_googlechrome_binary_symlink(host):
    """
    Tests if google-chrome binary is a symlink type.
    """
    assert host.file(PACKAGE_BINARY).is_symlink


def test_googlechrome_binary_which(host):
    """
    Tests the output to confirm google-chrome's binary location.
    """
    assert host.check_output('which google-chrome') == PACKAGE_BINARY


def test_googlechrome_repo_exists(host):
    """
    Tests if google-chrome-stable repo file exists for DEBIAN/EL systems.
    """
    assert host.file(DEBIAN_REPO_FILE).exists or \
        host.file(EL_REPO_FILE).exists


def test_googlechrome_repo_file(host):
    """
    Tests if google-chrome-stable repo file for DEBIAN/EL systems is file type.
    """
    assert host.file(DEBIAN_REPO_FILE).is_file or \
        host.file(EL_REPO_FILE).is_file
