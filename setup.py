# check if docker is installed

import os
import shutil

if os.system('docker --version') != 0:
    print('Docker is not installed. Please install docker first.')
    print('If Docker is installed, make sure it is in your PATH.')
    exit(1)

# build the docker image
os.system('docker build -t andrerc1/ansible ./ansible')
#os.system('docker build -t andrerc1/pi-emulator ./PiEmulator') could be added if we want to use diet pi instead of raspbian

# start the docker compose
if shutil.which('docker-compose') is None:
    print('using new docker compose command')
    os.system('docker compose up -d')
else:
    os.system('docker-compose up -d')

