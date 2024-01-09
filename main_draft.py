#main
#The master controller for all actions on this pico node.
#

#Base imports
import node
import network
import socket
from time import sleep
import machine

#Global variables

#Define the supported actions, along with default settings
#Todo: Later this will be converted to a json object
#
# Current schema for supported actions.  (name,on/off,repeat)
# example, ["ledstrip_fire",True,True] = ledstrip_fire action is "on" by default, and repeats with each loop
supported_actions = [["ledstrip_fire",True,True]]


#Connect to the network
try:
    node.connect()
except KeyboardInterrupt:
    machine.reset()
