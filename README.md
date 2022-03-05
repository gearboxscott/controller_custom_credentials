env:
  ENV_CUSTOM_CREDENTIAL_PASSWORD: '{{ password }}'
  ENV_CUSTOM_CREDENTIAL_USERNAME: '{{ username }}'
  ENV_CUSTOM_CREDENTIAL_PUBLIC_SSH_KEY: '{{ public_ssh_key }}'
  ENV_CUSTOM_CREDENTIAL_PRIVATE_SSH_KEY: '{{ private_ssh_key }}'
  
controller_custom_credentials Project
=========

A brief description of the project controller_custom_credentials goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the project should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

controller_custom_credentials Variables
--------------

A description of the settable variables for this project should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

controller_custom_credentials Project Playbook
----------------

Including an example of how to use your project (for instance, with variables passed in as parameters) is always nice for users too:

    - name: Project controller_custom_credentials
      hosts: all
      gather_facts: no
    
      tasks:
     - name: some role
        include_role:
          name: some role
          apply:
            tags:
              - some tag
        vars:
          # add variables if needed else delete entire section
        tags:
          - always

License
-------

GPL

Author Information
------------------

An optional section for the project authors to include contact information, or a website (HTML is not allowed).
