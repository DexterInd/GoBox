########################################################################
# this morse code generator uses new concepts: 
# 
########################################################################
from easygopigo import *
from gopigo import *
from time import sleep
from datetime import datetime

import atexit
@atexit.register
def cleanup():
    print("Cleanup")
    play_morse_msg()
    my_buzzer.sound_off()
    stop()
    print("Goodbye!")

    
def play_morse_msg():
    '''
    goes through the message list and plays it out
    '''
    for duration in message:
        my_buzzer.sound_on()
        sleep(duration)
        my_buzzer.sound_off()
        sleep(0.5)

def button_down():
    '''
    '''
    global start_msg
    print("Start recording")
    start_msg = datetime.now()
    recording = True

def button_up():
    '''
    '''
    print("Stop recording")
    end_msg = datetime.now()
    message.append((end_msg - start_msg).total_seconds())
    recording = False

# Create the message list
message = []
silence = []

# Create the buzzer
my_buzzer = Buzzer()

# the button sensor is a digital sensor, its default would be port D11
# but we have it in port A1, so we need to specify it.
my_button = ButtonSensor("A1")
my_button.up_call = button_up
my_button.down_call = button_down

# Get the message from the user
print("Press the button as you need to generate your morse code message")
print("Press Ctrl-C when the message is done")
print("It will then be played back")

recording = False
status = my_button.read()

while True:
    status = my_button.read()
    if status == 1:
        if not recording:
            recording = True
            start_msg = datetime.now()
            my_buzzer.sound_on()
    elif status == 0:
        if recording:
            recording = False
            my_buzzer.sound_off()
            end_msg = datetime.now()
            elapsed_time = (end_msg - start_msg).total_seconds()
            message.append(elapsed_time)
    sleep(0.5)


