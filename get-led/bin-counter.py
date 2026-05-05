import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)
leds_pins = [16, 12, 25, 17, 27, 23, 22, 24]
up_pin = 9
down_pin = 10

gpio.setup(leds_pins, gpio.OUT)
gpio.setup(up_pin, gpio.IN)
gpio.setup(down_pin, gpio.IN)

gpio.output(leds_pins, 0)

number = 0

def dec2bin(value):
    '''
Function, return a value as list of figure in binary forem
    '''
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if gpio.input(up_pin):
        print(f"Number is {number}, binary form is {dec2bin(number)}")
        number += 1
        time.sleep(0.2)
    if gpio.input(down_pin):
        print(f"Number is {number}, binary form is {dec2bin(number)}")
        number -= 1
        time.sleep(0.2)
    if number >= 256 or number < 0:
        print("Number exit from 8 bit value")
        number = 0
    gpio.output(leds_pins, dec2bin(number))