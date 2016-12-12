import gobox
import gopigo
import time
import atexit

@atexit.register
def cleanup():
    gopigo.stop()
    my_buzzer.sound_off()

# let's create a buzzer on port D11
my_buzzer = gobox.Buzzer("D11")
my_buzzer.sound_off()


# the range function starts with the first number, 
# but stops just short of the second number,
# here, 30 will never be reached.
for sound_power in range(1,250):
    print (sound_power)
    my_buzzer.sound(sound_power)
    time.sleep(0.01)

# counting down we have to start with 29, as 30 is not reached
# and we stop at 1, but we have to give 0 as the value not to be reached
# the third number is the skip count, 
# here -1 indicates counting backwards
for sound_power in range(29,0,-1):
    print (sound_power)
    my_buzzer.sound(sound_power)
    time.sleep(0.01)
