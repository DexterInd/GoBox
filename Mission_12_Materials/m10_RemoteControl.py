from easygopigo import *
from gopigo import *
from time import sleep
import atexit               # library that will give us a nice exit


@atexit.register
# this registers a function that will be called
# each time the code ends, and regardless
# of why it ends (intentional or not)
def cleanup():
    stop()  # we want the gopigo to stop
    print ("Good bye!")


# this is a variable that holds our security distance
# you may want to change it to get it more sensitive, or less
distance_to_stop = 20

# name the ultrasonic sensor
my_distance = UltraSonicSensor("A1")
# set our safe distance
my_distance.set_safe_distance(20)

my_remote = Remote("SERIAL")

# this is strictly to ensure that the IR Receiver is enabled
# we quit rather abruptly
if not my_remote.is_enabled():
    exit()

# Give user some information on what to do
print "Press any button on the remote to control the GoPiGo"
print "Use the * or the # to end the program"

# infinite loop
while True:

    # check if there's something in front
    # if there is, stop, even if GoPiGo is going backward
    # the GoPiGo will stop if the cat walks in front of it while
    #   it's going backward
    # your chosen behavior may be different
    if my_distance.is_too_close():
        stop()

    code = my_remote.get_remote_code()

    # handle the key presses and control the GoPiGo
    if code != -1 and len(code) != 0:
        if code == 'KEY_UP':
            # check if it's safe to go forward first.
            # the distance
            if not my_distance.is_too_close():
                forward()
        elif code == 'KEY_DOWN':
            backward()
        elif code == 'KEY_OK':
            stop()
        elif code == "KEY_LEFT":
            left()
        elif code == "KEY_RIGHT":
            right()
        elif code == 'KEY_H' or code == 'KEY_S':
            exit(0)

    sleep(0.1)
