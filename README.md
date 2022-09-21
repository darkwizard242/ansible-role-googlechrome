[![build-test](https://github.com/darkwizard242/ansible-role-googlechrome/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-googlechrome/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-googlechrome/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-googlechrome/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/43354?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43354?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43354?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-googlechrome&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-googlechrome) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-googlechrome&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-googlechrome) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-googlechrome&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-googlechrome) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-googlechrome&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-googlechrome) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-googlechrome?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-googlechrome?color=orange&style=flat-square)

# Ansible Role: googlechrome

Role to install (_by default_) [google-chrome-stable](https://www.google.com/chrome/) package for Debian based and EL based systems or uninstall (_if passed as var_) on **Debian** based and **EL** based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
googlechrome_app: google-chrome-stabl
googlechrome_desired_state: present
googlechrome_gpg_key: https://dl.google.com/linux/linux_signing_key.pub
googlechrome_repo_desired_state: present
googlechrome_repo_debian: deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main
googlechrome_repo_debian_filename: google-chrome
googlechrome_repo_el: http://dl.google.com/linux/chrome/rpm/stable/x86_64
googlechrome_repo_el_name: google-chrome
googlechrome_repo_el_description: google-chrome
googlechrome_repo_el_gpgcheck: yes
googlechrome_repo_el_enabled: yes
googlechrome_repo_el_filename: google-chrome
```

### Variables table:

Variable                          | Description
--------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------
googlechrome_app                  | Defines the app to install i.e. **google-chrome-stable**
googlechrome_desired_state        | Defined to dynamically set whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`
googlechrome_gpg_key              | GPG key for Google Chrome
googlechrome_repo_desired_state   | State for repo to download Google Chrome from. Can either be 'present' or 'absent'.
googlechrome_repo_debian          | Google Chrome's repo link for Debian based systems.
googlechrome_repo_debian_filename | Name of file to save for googlechrome's repo in `/etc/apt/sources.list.d/`
googlechrome_repo_el              | Google Chrome's repo link for EL based systems.
googlechrome_repo_el_name         | Google Chrome repo name for EL based systems.
googlechrome_repo_el_description  | Description for Google Chrome's repo for EL based systems.
googlechrome_repo_el_gpgcheck     | Boolean operation for performing gpg check against gpg key. Can either be **yes** or **no**.
googlechrome_repo_el_enabled      | Boolean operation for setting repository to enabled or disabled. Can either be **yes** or **no**.
googlechrome_repo_el_filename     | Name of file to save for googlechrome's repo in `/etc/yum.repos.d/`

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **google-chrome-stable** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.googlechrome
```

For customizing behavior of role (i.e. installation of latest **google-chrome-stable** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.googlechrome
  vars:
    googlechrome_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **google-chrome-stable** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.googlechrome
  vars:
    googlechrome_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-googlechrome/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
