#! /bin/bash
# Copyright Dexter Industries, 2015.
# Install the Troubleshooting GUI.
# Dev Notes:
# Helpful Link on Bin Paths:  http://www.cyberciti.biz/faq/how-do-i-find-the-path-to-a-command-file/

# updated from --force-yes to --yes --force-yes (2nd answer here: http://superuser.com/questions/164553/automatically-answer-yes-when-using-apt-get-install)
sudo apt-get --purge remove python-wxgtk2.8 python-wxtools wx2.8-i18n -y
sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n --yes --force-yes
sudo apt-get install python-psutil --yes --force-yes
sudo apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n --yes --force-yes

# Copy shortcut to desktop.
sudo rm /home/pi/Desktop/Troubleshooting_Start.desktop
sudo cp /home/pi/Desktop/GoBox/Troubleshooting_GUI/Troubleshooting_Start.desktop /home/pi/Desktop
# Make shortcut executable
sudo chmod +x /home/pi/Desktop/Troubleshooting_Start.desktop
# Make troubleshooting_start executable.
sudo chmod +x /home/pi/Desktop/GoBox/Troubleshooting_GUI/Troubleshooting_Start.sh