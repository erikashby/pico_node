#main module
#This module will run automatically when the pico starts up

#Define the possible actions that are supported by the pico

#create a fire
ledstrip_fire = __import__('/actions/ledstrip_fire.py', globals(), locals(), ['main'], 0)
ledstrip_fire.main()