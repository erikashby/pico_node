# We Geek Together action

# action: ledstrip_fire
#
# This action will simulate a fire with an RGB LED strip


# This action requires 
# - neopixel.py to be in the root folder since it provides the interface to the RGB strip
# - time for sleep actions

import time,sys,random
sys.path.append('/actions')
from neopixel import Neopixel

def main():  # Main function.
    # Default Configuration.  (In the future this will be handled through a config file)
    # Default number of led lights on strip
    led_strip_len = 60
    middle = int(led_strip_len/2)

    # Default IO pin used for led strip
    pico_gpio = 22
    
    #initilise strip
    pixels = Neopixel(led_strip_len, 0, pico_gpio, "GRB")
    
    brightness_adjustment = 0
    red=[255,0,0]
    yellow=[150,25,0]
    bright = 255
    medium = 100
    brightness_adjustment = 0
    rotate_adjustment = 0
    
    pixels.set_pixel_line_gradient(0, middle, yellow,red)
    pixels.set_pixel_line_gradient(middle, middle, yellow,red)
    

    while True:
        brightness_adjustment=random.randint(0,20)
        sleep_time=random.random()/3
        pixels.brightness(medium-brightness_adjustment)
        pixels.set_pixel_line_gradient(0, 59, yellow,red)
        pixels.rotate_right(rotate_adjustment)
        rotate_adjustment = rotate_adjustment + 1
        if rotate_adjustment > led_strip_len:
            rotate_adjustment=0
        pixels.show()
        time.sleep(sleep_time)
    
main()