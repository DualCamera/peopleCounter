# Experiments

## Requirements

* Raspberry Pi 3 Model B v1.2
* Raspberry Pi OS Lite (https://www.raspberrypi.org/software/operating-systems/)
* OpenCV

### Expand filesystem

### Dependencies

$ sudo apt update && sudo apt dist-upgrade
$ sudo apt install libgtk-3-0
$ sudo apt install libavcodec58 libavformat58
$ sudo apt install liblapack3
$ sudo apt install libwebp6 libtiff5 libopenjp2-7 
$ sudo apt install libilmbase23 libopenexr23 libswscale5 libatlas3-base
$ sudo apt install python3-venv

### Python virtual environment and OpenCV

In your python 3 workspace (e.g. /home/user/camera) create a virtual environment with:

$ python3 -m venv .venv
$ source .venv/bin/activate

Upgrade pip:

$ pip install --upgrade pip

# Install OpenCV

OpenCV will be installed on the virtual environment, as follows:

$ pip3 install opencv-python
