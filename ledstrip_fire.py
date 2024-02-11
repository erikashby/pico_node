# We Geek Together action

# action: ledstrip_fire
#
# This action will simulate a fire with an RGB LED strip


# This action requires 
# - neopixel.py to be in the root folder since it provides the interface to the RGB strip
# - time for sleep actions

import utime,sys,random
from time import sleep
import uasyncio as asyncio
#sys.path.append('/actions')
from neopixel import Neopixel

#define global configuration
# Default number of led lights on strip
global led_strip_len
led_strip_len=120

global middle
middle = int(led_strip_len/2)

# Default IO pin used for led strip
global pico_gpio
pico_gpio = 22
    
#color strip
global pixels
pixels = Neopixel(led_strip_len, 0, pico_gpio, "GRB")
    
#Initiage main colors and brighness
global red, yellow, black, bright, medium, rotate_adjustment, brightness_adjustment
red=[255,0,0]
yellow=[150,25,0]
black=[0,0,0]
bright = 255
medium = 100
rotate_adjustment = 0
brightness_adjustment = 0


def show_line(bright_level,color1,color2,rotate):  # Common function that will show a line from one color to the next
    
    pixels.brightness(bright_level)
        
    pixels.set_pixel_line_gradient(0, middle, color1,color2)
    pixels.set_pixel_line_gradient(middle, led_strip_len-1, color2,color1)
            
    #rotate line
    pixels.rotate_right(rotate)
    pixels.show()



def initialze(): #this is the 
    #Initilize flame line
    print("starting fire")
    show_line(medium,yellow,red,rotate_adjustment)

def off():
    show_line(0,black,black,0)

def main():  # Main function.
    #Pick a random brightness adjustment and a random time to stay on the current brightness
    global rotate_adjustment
    
    brightness_adjustment=random.randint(0,20)
    sleep_time=random.random()/3
        
    #Prepare the strip
    show_line(medium-brightness_adjustment,yellow,red,rotate_adjustment)

    #advance line to next position
    rotate_adjustment = rotate_adjustment + 1
    if rotate_adjustment > led_strip_len:
        rotate_adjustment=0
            
    sleep(sleep_time)
        
    #burst flicker
    if int(random.randint(0,20)) == 1:
        show_line(bright-brightness_adjustment-25,yellow,red,rotate_adjustment)
        sleep(0.02)
        show_line(bright-brightness_adjustment,yellow,red,rotate_adjustment)
        sleep(.01)
        show_line(bright-brightness_adjustment-25,yellow,red,rotate_adjustment)
        sleep(.01)
        show_line(bright-brightness_adjustment-70,yellow,red,rotate_adjustment)
        sleep(sleep_time)



#Main program
#initialze()  #Initialize the row
def main_loop():
    while True:  #Loop the main function
        main()