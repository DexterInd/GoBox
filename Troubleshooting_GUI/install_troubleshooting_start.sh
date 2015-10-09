#! /bin/bash
# Copyright Dexter Industries, 2015.
# Install the Troubleshooting GUI.
# Dev Notes:
# Helpful Link on Bin Paths:  http://www.cyberciti.biz/faq/how-do-i-find-the-path-to-a-command-file/

sudo apt-get --purge remove python-wxgtk2.8 python-wxtools wx2.8-i18n -y
sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n --force-yes
sudo apt-get install python-psutil --force-yes
sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n --force-yes

# Copy shortcut to desktop.
cp /home/pi/Desktop/GoBox/Troubleshooting_GUI/Troubleshooting_Start.desktop /home/pi/Desktop
# Make shortcut executable
sudo chmod +x /home/pi/Desktop/Troubleshooting_Start.desktop
# Make troubleshooting_start executable.
sudo chmod +x /home/pi/Desktop/GoBox/Troubleshooting_GUI/Troubleshooting_Start.sh