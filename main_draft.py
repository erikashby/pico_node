#main
#The master controller for all actions on this pico node.
#

#Base imports
import node
import network
import socket
from time import sleep
import machine
import json

#Global variables

#Define the supported actions, along with default settings
#Todo: Later this will be converted to a json object
#
# Current schema for supported actions.  (name,on/off,repeat)
# example, ["ledstrip_fire",True,True] = ledstrip_fire action is "on" by default, and repeats with each loop
# supported_actions = [["ledstrip_fire",True,True]]

get_actions = open("supported_actions.json")
actions = json.load(get_actions)
get_actions.close()


#Connect to the network
try:
    ip= node.connect()
except KeyboardInterrupt:
    machine.reset()

#Start socket

    
#Initilize actions
ledstrip_fire = __import__('/actions/ledstrip_fire.py', globals(), locals(), ['main','initilize'], 0)
ledstrip_fire.initilize()

#perform the main loop
while True:
    # actions[a = action array][2 = if looping]
    for a in actions:
        if a[2]:
            ledstrip_fire.main()
    
    #check socket for incomming command
