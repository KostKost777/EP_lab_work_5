import time
import RPi.GPIO as GPIO
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time

if __name__ == "__main__":
    dynamic_range = float(input("Введите динамический диапазон ЦАП (В): "))
    duration = float(input("Введите продолжительность измерений (с): "))
    
    adc = R2R_ADC(dynamic_range, compare_time=0.0001, verbose=False)
    
    voltage_values = []
    time_values = []
    
    try:
        start_time = time.time()
        
        while time.time() - start_time < duration:
            voltage = adc.get_sc_voltage()
            current_time = time.time() - start_time
            
            voltage_values.append(voltage)
            time_values.append(current_time)
            
            print(f"t = {current_time:.3f} с, U = {voltage:.3f} В")
        
        plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
        
    finally:
        del adc