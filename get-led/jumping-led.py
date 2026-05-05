import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)
leds_pins = [24, 22, 23, 27, 17, 25, 12, 16]

gpio.setup(leds_pins, gpio.OUT)

gpio.output(leds_pins, 0)

light_time = 0.2

while True:
    for led_pin in leds_pins[0:-1]:
        gpio.output(led_pin, 1)
        time.sleep(light_time)
        gpio.output(led_pin, 0)
    for led_pin in reversed(leds_pins[1:]):
        gpio.output(led_pin, 1)
        time.sleep(light_time)
        gpio.output(led_pin, 0)
    