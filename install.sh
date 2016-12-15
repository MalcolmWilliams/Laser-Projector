#!/bin/bash
sudo apt-get -y install git
git clone https://github.com/MalcolmWilliams/Laser-Writer.git
sudo apt-get -y install qjackctl
sudo usermod -a -G audio pi
#need to log out for the previous command to take effect
logout
