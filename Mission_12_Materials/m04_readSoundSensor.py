########################################################################
# this code only reads values from the sound sensor and 
# prints them to the screen
########################################################################

from easygopigo import *
from time import sleep
import atexit

# it's probably not necessary to have this here
# as the gopigo is never told to move
@atexit.register
def cleanup():
   print("Good bye!")
   stop()

# let's name the sound sensor and identify it
# as being the sensor in port A1
mySoundSensor=SoundSensor("A1")

# to get out of a forever loop like this one
# you will need to type in Ctrl-C on the keyboard
print("Use Ctrl-C to get out of the forever loop")
while True:
	# read the sensor 
    soundValue = mySoundSensor.read()
    # print the value
    print(soundValue)
    # wait a bit
    sleep(1)
