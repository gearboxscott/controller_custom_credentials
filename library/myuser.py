#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright: (c) 2012, Stephen Fromm <sfromm@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        name=dict(type='str', required=True, aliases=['user']),
        password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', default='present', choices=['absent', 'present'])
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )


    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    result['username'] = module.params['name']
    result['password'] = 'NOT_LOGGIN_PASSWORD'
    result['state'] = module.params['state']

    module.exit_json(**result)

def main():
    run_module()

# import module snippets
if __name__ == '__main__':
    main()
