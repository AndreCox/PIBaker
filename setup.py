# check if docker is installed

import os

if os.system('docker --version') != 0:
    print('Docker is not installed. Please install docker first.')
    print('If Docker is installed, make sure it is in your PATH.')
    exit(1)

# build the docker image
os.system('docker build -t andrerc1/ansible ./ansible')
#os.system('docker build -t andrerc1/pi-emulator ./PiEmulator') could be added if we want to use diet pi instead of raspbian

# start the docker compose
os.system('docker-compose up -d')

