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
        
        # График напряжения
        plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
        
        # Гистограмма периодов измерений
        if len(time_values) > 1:
            # Вычисляем периоды между измерениями
            periods = []
            for i in range(1, len(time_values)):
                period = time_values[i] - time_values[i-1]
                periods.append(period)
            
            # Строим гистограмму
            plt.figure(figsize=(10, 6))
            plt.hist(periods, bins=20, edgecolor='black', alpha=0.7)
            plt.xlabel('Период измерения (с)', fontsize=12)
            plt.ylabel('Количество измерений', fontsize=12)
            plt.title('Распределение количества измерений по продолжительности', fontsize=14)
            plt.grid(True, alpha=0.3)
            
            # Добавляем среднее значение
            avg_period = sum(periods) / len(periods)
            plt.axvline(avg_period, color='r', linestyle='--', linewidth=2, 
                       label=f'Средний период: {avg_period:.4f} с')
            plt.legend()
            
            # Выводим статистику
            print(f"\n=== Статистика периодов измерений ===")
            print(f"Всего измерений: {len(time_values)}")
            print(f"Средний период: {avg_period:.4f} с")
            print(f"Минимальный период: {min(periods):.4f} с")
            print(f"Максимальный период: {max(periods):.4f} с")
            print(f"Разброс: {(max(periods) - min(periods)):.4f} с")
            
            plt.show()
        else:
            print("Недостаточно данных для построения гистограммы")
        
    except KeyboardInterrupt:
        print("\nИзмерения прерваны пользователем")
    finally:
        adc.deinit()