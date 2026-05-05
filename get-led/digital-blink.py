import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
led_pin = 26

GPIO.setup(led_pin, GPIO.OUT)

period = 1.0
state = 0

while True:
    GPIO.output(led_pin, state)
    time.sleep(period)
    state = not state