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
import sys
from actions import ledstrip_fire


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
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

    
#Initilize actions
#ledstrip_fire = __import__('/actions/ledstrip_fire.py', globals(), locals(), ['main','initilize'], 0)
ledstrip_fire.initialze()

#perform the main loop
while True:

    cl, addr = s.accept()
    try:
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)

        request = str(request)
        led_on = request.find('/on')
        led_off = request.find('/off')
        print( 'led on = ' + str(led_on))
        print( 'led off = ' + str(led_off))
        
        stateis = "Hello World"

        response = stateis

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')
    
    
    ## actions[a = action array][2 = if looping]
    #for a in actions:
    #    if a[2]:
    #        ledstrip_fire.main()
    #
    #check socket for incomming command
