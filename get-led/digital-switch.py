import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
led_pin = 26
btn_pin = 13

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(btn_pin, GPIO.IN)

state = 0

while True:
    if GPIO.input(btn_pin):
        GPIO.output(led_pin, state)
        state = not state
        time.sleep(0.2)