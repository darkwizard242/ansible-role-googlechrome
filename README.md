
Ansible Role: googlechrome
=========

Role to install (_by default_) `google-chrome-stable` package for Debian based and EL based systems  or uninstall (_if  passed as var_)  on **Debian** based and **EL** based systems.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below (located in  `defaults/main.yml`):

```yaml
googlechrome_app: google-chrome-stabl
googlechrome_desired_state: present
googlechrome_gpg_key: https://dl.google.com/linux/linux_signing_key.pub
googlechrome_repo_desired_state: present
googlechrome_repo_debian: deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main
googlechrome_repo_debian_filename: google-chrome
googlechrome_repo_el: http://dl.google.com/linux/chrome/rpm/stable/x86_64
googlechrome_repo_el_name: google-chrome
googlechrome_repo_el_description: google-chrome
googlechrome_repo_el_gpgcheck: yes
googlechrome_repo_el_enabled: yes
googlechrome_repo_el_filename: google-chrome
```

Variable `googlechrome_app`: Defines the app to install i.e. **google-chrome-stable**

Variable `googlechrome_desired_state`: Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package.

Variable `googlechrome_gpg_key`: GPG key for Google Chrome

Variable `googlechrome_repo_desired_state`: State for repo to download Google Chrome from. Can either be 'present' or 'absent'.

Variable `googlechrome_repo_debian`: Google Chrome's repo link for Debian based systems.

Variable `googlechrome_repo_debian_filename`: Name of file to save for googlechrome's repo in `/etc/apt/sources.list.d/`

Variable `googlechrome_repo_el`: Google Chrome's repo link for EL based systems.

Variable `googlechrome_repo_el_name`: Google Chrome repo name for EL based systems.

Variable `googlechrome_repo_el_description`: Description for Google Chrome's repo for EL based systems.

Variable `googlechrome_repo_el_gpgcheck`: Boolean operation for performing gpg check against gpg key. Can either be **yes** or **no**.

Variable `googlechrome_repo_el_enabled`: Boolean operation for setting repository to enabled or disabled. Can either be **yes** or **no**.

Variable `googlechrome_repo_el_filename`: Name of file to save for googlechrome's repo in `/etc/yum.repos.d/`

Dependencies
------------

None

Example Playbook
----------------

For default behaviour of role (i.e. installation of **google-chrome-stable** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.googlechrome
```

For customizing behavior of role (i.e. installation of latest **google-chrome-stable** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.googlechrome
      vars:
        googlechrome_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **google-chrome-stable** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.googlechrome
      vars:
        googlechrome_desired_state: absent
```

License
-------

[MIT](https://github.com/darkwizard242/ansible-role-googlechrome/blob/master/LICENSE)

Author Information
------------------

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
