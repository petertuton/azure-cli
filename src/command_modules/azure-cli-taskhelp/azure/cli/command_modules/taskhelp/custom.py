# pylint: disable=no-self-use,too-few-public-methods
from __future__ import print_function
from azure.cli._locale import L

class TaskHelpCommands(object):

    def __init__(self, **_):
        pass

    def deploy_arm_template(self):
        '''How to deploy an ARM template using Azure CLI.'''
        print(L("""
***********************
ARM Template Deployment
***********************

Could this be helpful?  Let us know!
====================================

1. First Step
2. Second Step

And you're done!
    """))
