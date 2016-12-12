
from easygopigo import *
from gopigo import *
from time import sleep
import atexit

@atexit.register
def cleanup():
    gopigo.stop()
    mybuzzer.sound_off()
    
# let's create a software buzzer so we can control it
mybuzzer = Buzzer()    

# Ask the user for how many seconds we need to wait
# and confirm back to the user how long we'll be waiting
how_long = int(raw_input("How many seconds before I need to buzz? "))
print("I will alert you in %d seconds" % how_long)

# wait for that many seconds
sleep(how_long)

# start buzzing
for i in range(5):
    mybuzzer.sound(254)
    left_rot()   # this line will make the robot spin in place
    sleep(5)
    mybuzzer.sound_off()
    stop()
    sleep(1)

