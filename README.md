controller_custom_credentials
=============================

Demostrate how to use controller custom credentials

Requirements
------------

Custom ansible modules that were created to demonstrate how not use variables in modules.

* `user_module_correct_way.py`
* `user_module_wrong_way.py`

Variables
---------

```
custom_credential_username
custom_credential_password
custom_credential_private_ssh_key
custom_credential_public_ssh_key
```

Custom Credential
-----------------
```yaml
- description: custom credential
  injectors:
    env:
      ENV_CUSTOM_CREDENTIAL_USERNAME: '{{ username }}'
    extra_vars:
      custom_credential_password: '{{ password }}'
      custom_credential_private_ssh_key: '{{ private_ssh_key }}'
      custom_credential_public_ssh_key: '{{ public_ssh_key }}'
      custom_credential_username: '{{ username }}'
  inputs:
    fields:
    - id: username
      label: username
      multiline: false
      secret: false
      type: string
    - id: password
      label: password
      multiline: false
      secret: true
      type: string
    - id: private_ssh_key
      label: private_ssh_key
      multiline: true
      secret: true
      type: string
    - id: public_ssh_key
      label: public_ssh_key
      multiline: true
      secret: true
      type: string
    required:
    - username
    - password
  kind: cloud
  name: custom_credential
  natural_key:
    kind: cloud
    name: custom_credential
    type: credential_type
```

Custom Credential Type
----------------------

```yaml

```

Dependencies
------------

None.

Project Playbook
----------------

Including an example of how to use your project (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
---
# site.yml for controller_custom_credentials

- name: Project controller_custom_credentials
  hosts: localhost
  gather_facts: no

  tasks:
  - name: Show Oops the Developer Exposed Protected Data
    user_module_wrong_way:
      name: '{{ custom_credential_username }}'
      password: '{{ custom_credential_password }}'
      private_ssh_key: '{{ custom_credential_private_ssh_key }}'
      public_ssh_key: '{{ custom_credential_public_ssh_key }}'
      state: present

  - name: Show the Developer Protected Valuable Sensitive Data
    user_module_correct_way:
      name: '{{ custom_credential_username }}'
      password: '{{ custom_credential_password }}'
      private_ssh_key: '{{ custom_credential_private_ssh_key }}'
      public_ssh_key: '{{ custom_credential_public_ssh_key }}'
      state: present
```

Job Output
----------

```java
PLAYBOOK: site.yml *************************************************************
1 plays in site.yml

PLAY [Project controller_custom_credentials] ***********************************
META: ran handlers

TASK [Show Oops the Developer Exposed Protected Data] **************************
[WARNING]: Module did not set no_log for password
ok: [localhost] => {
    "changed": false,
    "invocation": {
        "module_args": {
            "name": "Haley_The_Dog",
            "password": "redhat123",
            "private_ssh_key": "-----BEGIN RSA PRIVATE KEY-----\\nsome private key data here\\n-----END RSA PRIVATE KEY-----",
            "public_ssh_key": "sh-rsa some publiic ssh key data here somename@somehost",
            "state": "present"
        }
    },
    "password": "OOPS_PASSWORD_WAS_EXPOSED",
    "private_ssh_key": "OOPS_PRIVATE_SSH_KEY_WAS_EXPOSED",
    "public_ssh_key": "OOPS_PE_SSH_KEY_WAS_EXPOSED",
    "state": "present",
    "username": "Haley_The_Dog"
}

TASK [Show the Developer Protected Valuable Sensitive Data] ********************
ok: [localhost] => {
    "changed": false,
    "invocation": {
        "module_args": {
            "name": "Haley_The_Dog",
            "password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
            "private_ssh_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
            "public_ssh_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
            "state": "present"
        }
    },
    "password": "NOT_LOGGIN_PASSWORD",
    "private_ssh_key": "NOT_LOGGIN_PRIVATE_KEY",
    "public_ssh_key": "NOT_LOGGIN_PUBLIC_KEY",
    "state": "present",
    "username": "Haley_The_Dog"
}
META: ran handlers
META: ran handlers

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

License
-------

GPL

Author Information
------------------

Scott Parker (sparker@redhat.com)
