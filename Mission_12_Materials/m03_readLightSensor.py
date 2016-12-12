
# helper libraries
from easygopigo import *
from time import sleep

# name the LightSensor so we can interact with it
my_light = LightSensor("A1")


# let's create a loop that will print out the value of the light sensor
# this will loop 20 times
# this is the same as Scratch REPEAT 20 TIMES
for i in range(20): 
    
    # access the light sensor, 
    # keep its value in a variable called sensorvalue
    sensorvalue = my_light.read()
    
    # print its value
    # this is the same as having the cat say the value
    print( sensorvalue)
    
    # wait half a second
    # this is the same as Scratch WAIT command
    sleep(0.5) 
    
