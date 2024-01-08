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

#define global configuration
# Default number of led lights on strip
led_strip_len = 60
middle = int(led_strip_len/2)

# Default IO pin used for led strip
pico_gpio = 22
    
#initilise strip
pixels = Neopixel(led_strip_len, 0, pico_gpio, "GRB")
    
#Initiage main colors and brighness
red=[255,0,0]
yellow=[150,25,0]
bright = 255
medium = 100



def show_line(bright_level,color1,color2,rotate):
    
    pixels.brightness(bright_level)
        
    pixels.set_pixel_line_gradient(0, middle, color1,color2)
    pixels.set_pixel_line_gradient(middle, led_strip_len-1, color2,color1)
            
    #rotate line
    pixels.rotate_right(rotate)
    pixels.show()


def main():  # Main function.
    brightness_adjustment = 0
    rotate_adjustment = 0

    #Initilize flame line
    show_line(medium,yellow,red,rotate_adjustment)
    
    #Main flicker loop.  This creates a flicker by (1- adjusting the brightness, and 2- rotating the two colors)
    while True:
        #Pick a random brightness adjustment and a random time to stay on the current brightness
        brightness_adjustment=random.randint(0,20)
        sleep_time=random.random()/3
        
        #Prepare the strip
        show_line(medium-brightness_adjustment,yellow,red,rotate_adjustment)

        #advance line to next position
        rotate_adjustment = rotate_adjustment + 1
        if rotate_adjustment > led_strip_len:
            rotate_adjustment=0
            
        time.sleep(sleep_time)
        
        #burst flicker
        if int(random.randint(0,20)) == 1:
            show_line(bright-brightness_adjustment-25,yellow,red,rotate_adjustment)
            time.sleep(0.02)
            show_line(bright-brightness_adjustment,yellow,red,rotate_adjustment)
            time.sleep(.01)
            show_line(bright-brightness_adjustment-25,yellow,red,rotate_adjustment)
            time.sleep(.01)
            show_line(bright-brightness_adjustment-70,yellow,red,rotate_adjustment)
            time.sleep(sleep_time)
        
        #pause for some random time

    
main()