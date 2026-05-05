import RPi.GPIO as GPIO

dynamic_range = 3.302

class PWM_DAC:
    def __init__(self, gpio_pin = 12, pwm_frequensy = 500, dynamic_range = 3.302, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequensy = pwm_frequensy
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(12, GPIO.OUT)  
        
        self.pwm = GPIO.PWM(gpio_pin, 1000)

        self.pwm.start(0.0)

    def deinit(self):
        GPIO.cleanup()

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            raise ValueError(f"Voltage out of range (0.00 - {self.dynamic_range:.2f} В)")
            return
        self.pwm.ChangeDutyCycle(voltage / self.dynamic_range * 100)


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, dynamic_range, True)

        while True:
            try:
                voltage = float(input("Input voltage in Volts:  "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Not a number. Try again.")
    finally:
        dac.deinit()
