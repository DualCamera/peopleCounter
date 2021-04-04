# Raspberry Pi 3 People Counter

https://www.youtube.com/watch?v=nu2k0yGO00Y&feature=youtu.be

## Requirements

* Raspberry Pi 3 Model B v1.2
* Raspberry Pi OS Lite (https://www.raspberrypi.org/software/operating-systems/)
* OpenCV

## OpenCV

More details on https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/  

### Expand filesystem

### Dependences

$ sudo apt-get update && sudo apt-get upgrade  
$ sudo apt-get install build-essential cmake pkg-config  
$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev  
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev  
$ sudo apt-get install libxvidcore-dev libx264-dev  
$ sudo apt-get install libfontconfig1-dev libcairo2-dev  
$ sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev  
$ sudo apt-get install libgtk2.0-dev libgtk-3-dev  
$ sudo apt-get install libatlas-base-dev gfortran  
$ sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103  
$ sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5  
$ sudo apt-get install python3-dev

### Python virtual environment and NumPy

$ wget https://bootstrap.pypa.io/get-pip.py  
$ sudo python3 get-pip.py  

$ sudo pip install virtualenv virtualenvwrapper  

Edit ~/.bashrc and append the following lines to the bottom of the file:  

export WORKON_HOME=$HOME/.virtualenvs  
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3  
source /usr/local/bin/virtualenvwrapper.sh  

Reload bashrc:  
$ source ~/.bashrc  

# virtualenv and virtualenvwrapper
Create Python 3 virtual environment:  
$ mkvirtualenv cv -p python3  

Install the PiCamera API  
$pip3 install "picamera[array]"  

### OpenCV Installation
$ cd ~  
$ wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.1.zip  
$ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.1.zip  
$ unzip opencv.zip  
$ unzip opencv_contrib.zip  
$ mv opencv-4.5.1 opencv  
$ mv opencv_contrib-4.5.1 opencv_contrib  

Edit the CONF_SWAPSIZ  variable in /etc/dphys-swapfile 
CONF_SWAPSIZE=2048

$ sudo /etc/init.d/dphys-swapfile stop  
$ sudo /etc/init.d/dphys-swapfile start  

for work in Virtual Enviroment  
$ workon cv  

Install numpy  
$ pip install numpy  

configure build  
$ cd ~/opencv  
$ mkdir build  
$ cd build  
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \  
    -D CMAKE_INSTALL_PREFIX=/usr/local \  
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \  
    -D ENABLE_NEON=ON \  
    -D ENABLE_VFPV3=ON \  
    -D BUILD_TESTS=OFF \  
    -D INSTALL_PYTHON_EXAMPLES=OFF \  
    -D OPENCV_ENABLE_NONFREE=ON \  
    -D CMAKE_SHARED_LINKER_FLAGS=-latomic \  
    -D BUILD_EXAMPLES=OFF ..  

$ make -j4  

$ sudo make install  
$ sudo ldconfig  

## Postgresql  

$ sudo apt-get install postgresql  
$ sudo apt-get install python-psycopg2  
$ sudo apt-get install libpq-dev  

$ pip install psycopg2  

Create Postgresql PI user  
$ sudo su postgres
$ createuser pi -P --interactive

Create database
$ psql
> create database peoplecounterdb;
