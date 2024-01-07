# We Geek Together action

# action: ledstrip_fire
#
# This action will simulate a fire with an RGB LED strip


# This action requires 
# - neopixel.py to be in the same folder since it provides the interface to the RGB strip
# - time for sleep actions

import time,sys
sys.path.append('/actions')
from neopixel import Neopixel

def main():  # Main function.
    # Default Configuration.  (In the future this will be handled through a config file)
    # Default number of led lights on strip
    led_strip_len = 60

    # Default IO pin used for led strip
    pico_gpio = 22
    
    brightness_adjustment = 0
    red=[255,0,0]
    yellow=[255,100,0]
    while True:
        pixels.fill(red)
        pixels.show()
        
    
    
main()