import time
import wx
import os
import pickle
from datetime import datetime
import subprocess
from collections import Counter
import threading
import psutil
import signal
import urllib2
		
def send_bash_command(bashCommand):
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE) #, stderr=subprocess.PIPE)
	output = process.communicate()[0]
	return output
	
class MainPanel(wx.Panel):
	""""""
	#----------------------------------------------------------------------
	def __init__(self, parent):
		"""Constructor"""
		
		wx.Panel.__init__(self, parent=parent)
		self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
		self.frame = parent
 
		sizer = wx.BoxSizer(wx.VERTICAL)
		hSizer = wx.BoxSizer(wx.HORIZONTAL)
		
		font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, u'Helvetica')
		self.SetFont(font)
		
		#-------------------------------------------------------------------
		# Standard Buttons
		y=20
		# Start Programming
		start_programming = wx.Button(self, label="Troubleshoot GoPiGo", pos=(25,y))
		start_programming.Bind(wx.EVT_BUTTON, self.start_programming)
		
		# Open Examples
		examples_button = wx.Button(self, label="Troubleshoot GrovePi", pos=(25, y+50))
		examples_button.Bind(wx.EVT_BUTTON, self.examples)			
		 
		#Update Curriculum
		curriculum_update = wx.Button(self, label="Demo GoPiGo", pos=(25,y+100))
		curriculum_update.Bind(wx.EVT_BUTTON, self.curriculum_update)

		# Exit
		exit_button = wx.Button(self, label="Exit", pos=(25,y+150))
		exit_button.Bind(wx.EVT_BUTTON, self.onClose)
		
		wx.StaticText(self, -1, "Caution: Do not close the terminal window!", (25, y+200))
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)		# Sets background picture
 
	#----------------------------------------------------------------------
	def OnEraseBackground(self, evt):

		dc = evt.GetDC()
 
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()	
		bmp = wx.Bitmap("/home/pi/Desktop/GoBox/Troubleshooting_GUI/dex.png")	# Draw the photograph.
		dc.DrawBitmap(bmp, 200, 0)						# Absolute position of where to put the picture

	def start_programming(self, event):
		dlg = wx.MessageDialog(self, 'Starting the tests. This might take a few minutes to complete.  Power the GoPiGo with the battery pack.  Turn the GoPiGo Upside Down.', 'Update', wx.OK|wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()
		
		send_bash_command('sudo chmod +x /home/pi/Desktop/GoPiGo/Troubleshooting/all_tests.sh')
		send_bash_command('sudo /home/pi/Desktop/GoPiGo/Troubleshooting/all_tests.sh')
		
		dlg = wx.MessageDialog(self, 'Tests Complete. Log has been saved to Desktop. Please copy it and send it by email or upload it on the forums', 'Update', wx.OK|wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()

	def curriculum_update(self, event):
		dlg = wx.MessageDialog(self, 'Demoing the GoPiGo. The LEDs should blink on the GoPiGo and it should move forward and back', 'Update', wx.OK|wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()

	
		send_bash_command('sudo python /home/pi/Desktop/GoPiGo/Software/Python/other_scripts/demo.py')

		dlg = wx.MessageDialog(self, 'Demo Complete', 'Update', wx.OK|wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()
		
	def examples(self, event):
		dlg = wx.MessageDialog(self, 'Starting the tests. This might take a few minutes to complete.', 'Update', wx.OK|wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()
	
		send_bash_command('sudo chmod +x /home/pi/Desktop/GrovePi/Troubleshooting/all_tests.sh')
		send_bash_command('sudo /home/pi/Desktop/GrovePi/Troubleshooting/all_tests.sh')
		
		dlg = wx.MessageDialog(self, 'Tests Complete. Log has been saved to Desktop. Please copy it and send it by email or upload it on the forums', 'Update', wx.OK|wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()
		
	def onClose(self, event):	# Close the entire program.
		self.frame.Close()
  
########################################################################
class MainFrame(wx.Frame):
	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		# wx.ComboBox

		wx.Icon('/home/pi/Desktop/GoBox/Troubleshooting_GUI/favicon.ico', wx.BITMAP_TYPE_ICO)
		wx.Log.SetVerbose(False)
		wx.Frame.__init__(self, None, title="Test Dexter Industries Hardware", size=(600,250))		# Set the fram size

		panel = MainPanel(self)        
		self.Center()
		
########################################################################
class Main(wx.App):
    #----------------------------------------------------------------------
    def __init__(self, redirect=False, filename=None):
        """Constructor"""
        wx.App.__init__(self, redirect, filename)
        dlg = MainFrame()
        dlg.Show()
		
if __name__ == "__main__":
	app = Main()
	app.MainLoop()
