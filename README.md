# PIBaker 🥧

### Create Custom Raspberry Pi Images Easily.

I realized that there was no easy way to create a customized Raspberry Pi image. This project was created to make custom images easily without the need for connecting to a real Pi. As well this project makes sure that your images are re-creatable incase you need to make updates and bug fixes in the future.

## Features

- 🐋 Cross-Platform Runs on Any machine
- 🖥️ Comes with a emulated Raspberry Pi, anything you can do on a regular Pi you can do here.
- 🤖 Uses Ansible which makes setting up the Pi simple.

## Dependencies

These need to be installed to use the program. You can use winget (windows) or apt-get (linux).

### [🐍 Python 3](https://www.python.org/downloads/)

- Windows `winget install python3`
- Linux `apt-get install python3`

### [🐋 Docker](https://www.docker.com/get-started/)

- Windows `winget install -e --id Docker.DockerDesktop`
- Linux [Docker Desktop](https://docs.docker.com/desktop/linux/install/ubuntu/)

## How to use

1. Clone or download the repository

`git clone --depth=1 https://github.com/AndreCox/PIBaker.git`

2. Move into the PIBaker directory

`cd PIBaker`

3. Run the setup.py script

`python setup.py`

4. Monitor the process with Docker Desktop (Optional)

Look for the stack called `pibaker` you can click on the stack and you should see 2 containers inside. You can monitor the Ansible container, when it is done both containers should stop.

5. A file called distro.img should appear in the dist folder. This is your final bootable image.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=andrecox/PiBaker&type=Date)](https://star-history.com/#andrecox/PiBaker&Date&theme=dark)

Thank you everyone for staring my project :)

## Note
I have had reports that M1 Macs have issues running this software, a work around for now is to run docker inside a Ubuntu VM.
