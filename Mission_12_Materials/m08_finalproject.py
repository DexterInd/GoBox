########################################################################
# this earthquake detector uses new concepts: 
# the list
# writing to a file
# 
########################################################################
from easygopigo import *
from gopigo import *
from time import sleep

import atexit
@atexit.register
def cleanup():
    stop()
    
# let's create an empty data list
earthquakeData = []

myMotionSensor = MotionSensor()

for i in range(100):  # loop 100 times
    current_earthquake = myMotionSensor.read()
    print (current_earthquake)
    earthquakeData.append(current_earthquake)
    time.sleep(0.25)


print(earthquakeData)

# write to a file
# the file will be on your Desktop
with open('/home/pi/Desktop/earthquakedata.txt', 'w') as f:
	for i in range(len(earthquakeData)):
		f.write(str(earthquakeData[i]))
		f.write("\n")  # this means a new line, or Enter key in a word processor
