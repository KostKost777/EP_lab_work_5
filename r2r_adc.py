import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    
    def __del__(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    
    def number_to_dac(self, number):
        for i in range(8):
            bit = (number >> (7 - i)) & 1
            GPIO.output(self.bits_gpio[i], bit)
    
    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                return number
        return 255
    
    def get_sc_voltage(self):
        digital_value = self.sequential_counting_adc()
        voltage = (digital_value / 255) * self.dynamic_range
        if self.verbose:
            print(f"Digital value: {digital_value}, Voltage: {voltage:.3f} V")
        return voltage

if __name__ == "__main__":
    dynamic_range = float(input("Enter the dynamic range of your DAC (V): "))
    
    try:
        adc = R2R_ADC(dynamic_range, verbose=True)
        
        while True:
            voltage = adc.get_sc_voltage()
            print(f"Measured voltage: {voltage:.3f} V")
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nMeasurement stopped by user")
    finally:
        del adc