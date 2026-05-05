import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose=False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose
    
    def deinit(self):
        self.bus.close()
    
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:x}, Младший байт: {lower_data_byte:x}, Число: {number}")
        return number
    
    def get_voltage(self):
        digital_value = self.get_number()
        voltage = (digital_value / 1023) * self.dynamic_range
        if self.verbose:
            print(f"Digital value: {digital_value}, Voltage: {voltage:.3f} V")
        return voltage

if __name__ == "__main__":
    dynamic_range = float(input("Введите динамический диапазон АЦП (В): "))
    
    try:
        adc = MCP3021(dynamic_range, verbose=True)
        
        while True:
            voltage = adc.get_voltage()
            print(f"Measured voltage: {voltage:.3f} V")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nMeasurement stopped by user")
    finally:
        adc.deinit()

Traceback (most recent call last):
  File "/home/b01-502/Desktop/Scripts/Reps/GET_ADC/EP_lab_work_5/mcp3021_driver.py", line 37, in <module>
    voltage = adc.get_voltage()
  File "/home/b01-502/Desktop/Scripts/Reps/GET_ADC/EP_lab_work_5/mcp3021_driver.py", line 24, in get_voltage
    digital_value = self.get_number()
  File "/home/b01-502/Desktop/Scripts/Reps/GET_ADC/EP_lab_work_5/mcp3021_driver.py", line 15, in get_number
    data = self.bus.read_word_data(self.address, 0)
OSError: [Errno 5] Input/output error