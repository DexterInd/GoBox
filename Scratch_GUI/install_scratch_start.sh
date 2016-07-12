#! /bin/bash
# Copyright Dexter Industries, 2015.
# Install the Scratch GUI.
# Dev Notes:
# Helpful Link on Bin Paths:  http://www.cyberciti.biz/faq/how-do-i-find-the-path-to-a-command-file/


# Copy shortcut to desktop.
cp /home/pi/Desktop/GoBox/Scratch_GUI/Scratch_Start.desktop /home/pi/Desktop
# sudo rm /usr/share/applications/scratch.desktop															# Remove the Scratch Start button in the Menu

######
# Added these to solve the menu problem of scratch.  Then removed them.  
# These are removed for now, the call up the Scratch Gui, not the scratch start.
# sudo rm /usr/share/raspi-ui-overrides/applications/scratch.desktop										# Remove the Scratch Start button in the Menu
# sudo cp /home/pi/Desktop/GoBox/Scratch_GUI/Scratch_Start.desktop /usr/share/applications/scratch.desktop						# Copy the Scratch_Start to the Menu
# sudo cp /home/pi/Desktop/GoBox/Scratch_GUI/Scratch_Start.desktop /usr/share/raspi-ui-overrides/applications/scratch.desktop		# Copy the Scratch_Start to the Menu
# sudo chmod 777 /usr/share/applications/scratch.desktop							# Menu Shortcut Permissions.
# sudo chmod 777 /usr/share/raspi-ui-overrides/applications/scratch.desktop		# Menu Shortcut Permissions.

# Make shortcut executable
sudo chmod +x /home/pi/Desktop/Scratch_Start.desktop							# Desktop shortcut permissions.

# Make run_scratch_gui executable.
sudo chmod +x /home/pi/Desktop/GoBox/Scratch_GUI/Scratch_Start.sh
# Make scratch start example read only.
sudo chmod ugo+r /home/pi/Desktop/GoBox/Scratch_GUI/new.sb	# user, group, etc are just read only
# Make select_state, error_log, nohup.out readable and writable
sudo chmod 777 /home/pi/Desktop/GoBox/Scratch_GUI/selected_state
sudo chmod 777 /home/pi/Desktop/GoBox/Scratch_GUI/error_log
sudo chmod 777 /home/pi/nohup.out

# Install Scratch Example Shortcuts for the Products
# This will creat symbolic links to the various example scripts.  https://blog.bartbania.com/raspberry_pi/create-symbolic-links-in-linux/
#ln -s /home/pi/Desktop/GrovePi/Software/Scratch/Grove_Examples/ GrovePi
#ln -s /home/pi/Desktop/GoPiGo/Software/Scratch/Examples/ GoPiGo
#ln -s /home/pi/Desktop/BrickPi_Scratch/Examples/ BrickPi

# Add the soft links that allows users to reach the Dexter Ind Scratch examples from within the Scratch interface

# BrickPi link
[ ! -d /usr/share/scratch/Projects/BrickPi ]  && sudo ln -s /home/pi/Desktop/BrickPi/Examples /usr/share/scratch/Projects/BrickPi

# GoPiGo link
[ ! -d /usr/share/scratch/Projects/GoPiGo ]  && sudo ln -s /home/pi/Desktop/GoPiGo/Software/Scratch/Examples /usr/share/scratch/Projects/GoPiGo

# GrovePi Link
[ ! -d /usr/share/scratch/Projects/GrovePi ]  && sudo ln -s /home/pi/Desktop/GrovePi/Software/Scratch/Grove_Examples /usr/share/scratch/Projects/GrovePi


# Remove Scratch Shortcuts if they're there.
sudo rm /home/pi/Desktop/BrickPi_Scratch_Start.desktop
sudo rm /home/pi/Desktop/GoPiGo_Scratch_Start.desktop
sudo rm /home/pi/Desktop/scratch.desktop

# Make sure that Scratch always starts Scratch GUI
# We'll install these parts to make sure that if a user double-clicks on a file on the desktop
# Scratch GUI is launched, and all other programs are killed.

#delete scratch from /usr/bin
sudo rm /usr/bin/scratch
# make a new scratch in /usr/bin
sudo cp /home/pi/Desktop/GoBox/Scratch_GUI/scratch /usr/bin
# Change scratch permissions
sudo chmod +x /usr/bin/scratch

# set permissions
# sudo chmod +x /home/pi/Desktop/GoBox/Scratch_GUI/scratch_launch
sudo chmod +x /home/pi/Desktop/GoBox/Scratch_GUI/scratch_direct
