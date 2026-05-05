import time
import matplotlib.pyplot as plt
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

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
        
        # Вычисляем периоды измерений
        periods = []
        for i in range(1, len(time_values)):
            period = time_values[i] - time_values[i-1]
            periods.append(period)
        
        # Строим график
        plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
        
        # Строим гистограмму периодов
        if periods:
            plt.figure()
            plt.hist(periods, bins=20, edgecolor='black')
            plt.xlabel('Период измерения (с)')
            plt.ylabel('Частота')
            plt.title('Распределение периода семплирования')
            plt.grid(True, alpha=0.3)
            plt.show()
        else:
            print("Недостаточно данных для построения гистограммы")
        
    except KeyboardInterrupt:
        print("\nИзмерения прерваны пользователем")
    finally:
        adc.deinit()