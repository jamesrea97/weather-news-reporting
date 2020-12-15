''' This module deploys the service in a new environment, install the dependencies required for the project '''
from pip._internal import main as pipmain


def deploy():
    ''' Method will install the dependencies required for this project '''

    print('Trying to install pip dependencies...')

    with open('dependencies/prod.txt') as file:
        dependencies = file.readlines()

        for dependency in dependencies:
            pipmain(['install', dependency])
