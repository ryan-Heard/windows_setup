import subprocess
from typing import List
import time

def read_file(file_name):
    commands = []

    with open(file_name, 'r') as f:
        for line in f:
            commands.append(line.rstrip())

    return commands


def run_commands(commands):

    for install in commands:
        install += ' -y'

        try:
            subprocess.run(install)
            print("Successfully installed {0}".format(install.split()[2]))
        except Exception as e:
            print("Could not run commands: {0}. \n Error: {1}".format(install, e))

if __name__ == '__main__':
    print('Starting to load software')
    commands = read_file('install_commands.txt')
    run_commands(commands)
    time.sleep(10)