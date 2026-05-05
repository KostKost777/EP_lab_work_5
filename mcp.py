import time
import matplotlib.pyplot as plt
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time

if __name__ == "__main__":
    dynamic_range = float(input("Введите динамический диапазон АЦП (В): "))
    duration = float(input("Введите продолжительность измерений (с): "))
    
    voltage_values = []
    time_values = []
    
    try:
        adc = MCP3021(dynamic_range, verbose=False)
        
        start_time = time.time()
        
        while time.time() - start_time < duration:
            voltage = adc.get_voltage()
            current_time = time.time() - start_time
            
            voltage_values.append(voltage)
            time_values.append(current_time)
            
            print(f"t = {current_time:.3f} с, U = {voltage:.3f} В")
            time.sleep(0.1)
        
        plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
        
        periods = [time_values[i] - time_values[i-1] for i in range(1, len(time_values))]
        rounded_periods = [round(p, 2) for p in periods]
        
        plt.figure()
        plt.hist(rounded_periods, bins=[0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15], edgecolor='black', align='left')
        plt.xlabel('Период измерения (с)')
        plt.ylabel('Количество измерений')
        plt.title('Гистограмма периода семплирования')
        plt.xticks([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15])
        plt.grid(True, alpha=0.3)
        plt.show()
        
    except KeyboardInterrupt:
        print("\nИзмерения прерваны пользователем")
    finally:
        adc.deinit()