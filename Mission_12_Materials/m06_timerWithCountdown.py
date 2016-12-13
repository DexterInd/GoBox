import time
import gobox
import gopigo
import atexit

@atexit.register
def cleanup():
    gopigo.stop
    mybuzzer.sound_off()
    
# The following is just a trick to ensure compatibility between Python 2 and 3
try:
    input = raw_input   #python 2
except NameError:
    pass    # python 3


# let's create a software buzzer so we can control it
mybuzzer = gobox.Buzzer()    

# Ask the user for how many seconds we need to wait
# and confirm back to the user how long we'll be waiting
# we also need to make sure we get a number back, hence the use of int
# in front of input
how_long = int(input("How many seconds before I need to buzz? "))
print("I will alert you in %d seconds" % how_long)

# following line reads as this:
# countdown = 10 if we have to count for more than 10 seconds
# otherwise limit the countdown to how long we have to count (less than 10)
countdown = 10 if how_long > 10 else how_long

# wait till we're 10 seconds before the end
time.sleep(how_long-countdown if how_long > 10 else 0 )

# do a countdown from the value of 'countdown' down to zero
for i in range(countdown,0,-1):
    print(i)
    mybuzzer.sound(5)
    time.sleep(0.01)
    mybuzzer.sound_off()
    time.sleep(1)
    
    
# sound the alarm by buzzing for 5 seconds
# then be quiet for one second
# and do that five times
# you could choose to do this forever instead
# by using a while True: statement
for i in range(5):
    mybuzzer.sound(254)
    gopigo.left_rot()
    time.sleep(5)
    mybuzzer.sound_off()
    time.sleep(1)

