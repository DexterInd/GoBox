from easygopigo import *
from gopigo import *
from time import sleep
import atexit


@atexit.register
# this registers a function that will be called
# each time the code ends, and regardless
# of why it ends (intentional or not)
def cleanup():
    stop()  # we want the gopigo to stop
    print ("Good bye!")

my_line = LineFollower("I2C")

while True:
    position = my_line.read_position()
    if position == "Right":
        turn_left(10)
    if position == "Left":
        turn_right(10)
    if position == "Center":
        forward(5)
    sleep(0.1)
