from easygopigo import *
from gopigo import *
from time import sleep
import atexit

@atexit.register
# this will be called if the program is killed via 
# a Ctrl-C on the keyboard or any other reason
def cleanup():
	stop()
	
	
# Let's start the GoPiGo. 
# this command only needs to be given once 
# GoPiGo will keep going forward until told to stop
print("Going forward")
forward()

# let's name our ultrasonic sensor
my_ultrasonic = UltraSonicSensor("A1")

# Note the absence of Wait code, or time.sleep in Python
# As GoPiGo is not using broadcast events in Python
# there's no need to space the queries out
# It's possible to loop as quickly as possible
# and get precise behavior.
print("To stop the forever loop, use Ctrl-C on the keyboard")
while True:
	dist = my_ultrasonic.read()

	# in case of error the above function can return a value of -1
	# there's a danger here if we simply check for less than 40 cm
	if dist > 0 and dist < 40:
		print("Object too close. Stopping!")
		stop()
		break  # this break forces the while loop to quit

