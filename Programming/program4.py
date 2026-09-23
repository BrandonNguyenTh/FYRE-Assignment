# Blinking program

# Incorperate/include modules
import machine #module with all the microcontroller stuff
import time #module with time methods

#make the led object
#Green led is GPIO Pin 0
led = machine.Pin(0, machine.Pin.OUT)

#infinite loop
while True:
  led.value(1) #turn on the LED
  time.sleep(.25) #0.25 second delay
  led.value(0) #turn off the LED
  time.sleep(0.25) #delay again
