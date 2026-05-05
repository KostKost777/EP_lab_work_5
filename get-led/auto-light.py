import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
led_pin = 26
light_pin = 6

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(light_pin, GPIO.IN)

while True:
    if GPIO.input(light_pin):
        GPIO.output(led_pin, 0)
        time.sleep(0.2)
    else:
        GPIO.output(led_pin, 1)