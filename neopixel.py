# CircuitPython demo - NeoPixel
import time
import board
import neopixel

pixel_pin = board.D5 # pwm pin, typically we use digital 5
pixel_pin2 = board.D6
num_pixels = 24
num_pixels2 = 12

led = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False) # brightness is in % 0.0-1.0 (0%-100%)
led2 = neopixel.NeoPixel(pixel_pin2, num_pixels2, brightness=1, auto_write=False) # brightness is in % 0.0-1.0 (0%-100%)

x = 0
y = 12
z = 25
green = [0, 255, 0]
off = 0
while True:
  if(x<=24):
    led[x] = green
    x+=1
    time.sleep(0.1)
    led.show()
    #if(x=24):
     #   z = 0
  if(y<=12):
    led2[x] = green
    y+=1
    time.sleep(0.1)
    led.show()
   '''if(z<=24):
       led[z]=off
       led.show()
       time.sleep(0.1)
       led[z] = green
       time.sleep(0.1)
       led.show()
       z+=1
    if(z=24):
        z=0'''