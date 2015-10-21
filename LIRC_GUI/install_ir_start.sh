#! /bin/bash
# Copyright Dexter Industries, 2015.
# Install the IR GUI
# Dev Notes:
# Helpful Link on Bin Paths:  http://www.cyberciti.biz/faq/how-do-i-find-the-path-to-a-command-file/

sudo apt-get --purge remove python-wxgtk2.8 python-wxtools wx2.8-i18n -y
sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n --force-yes
sudo apt-get install python-psutil --force-yes
sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n --force-yes

# Copy shortcut to desktop.
cp /home/pi/Desktop/GoBox/LIRC_GUI/ir_start.desktop /home/pi/Desktop
# Make shortcut executable
sudo chmod +x /home/pi/Desktop/ir_start.desktop
# Make ir_start.sh executable.
sudo chmod +x /home/pi/Desktop/GoBox/LIRC_GUI/ir_start.sh
sudo python setup.py install