from neopixel import Neopixel
import time

pixels = Neopixel(120, 0, 22, "GRB")
pixels.fill((100, 50, 0))
#pixels.set_pixel(5, (255, 0, 0))
#pixels.show()
pos = 0
brightness = 0

pixels.brightness(100)
while True:
    pixels.fill((255, 100, 0))
    pixels.show()
    time.sleep(.05)
    pixels.fill((220, 40, 0))
    #pixels.fill((0, 255, 255))
    pixels.set_pixel(pos+5, (100, 10, 10))
    pixels.set_pixel(pos+10, (100, 10, 10))
    pixels.set_pixel(pos - 1, (100, 10, 10))
    pixels.show()
    time.sleep(.10)
    pos = pos + 1
    if pos > 100:
        pos = 0