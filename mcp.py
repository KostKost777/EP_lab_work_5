import time
import matplotlib.pyplot as plt
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time

def plot_sampling_period_hist(time_values):
    """
    Строит гистограмму распределения количества измерений по их продолжительности
    """
    if len(time_values) < 2:
        print("Недостаточно данных для построения гистограммы")
        return
    
    periods = []
    for i in range(1, len(time_values)):
        period = time_values[i] - time_values[i-1]
        periods.append(period)
    
    plt.figure(figsize=(10, 6))
    plt.hist(periods, bins=20, edgecolor='black', alpha=0.7, color='blue')
    plt.xlabel('Период измерения (с)', fontsize=12)
    plt.ylabel('Количество измерений', fontsize=12)
    plt.title('Гистограмма периода семплирования', fontsize=14)
    plt.grid(True, alpha=0.3)
    
    avg_period = sum(periods) / len(periods)
    plt.axvline(avg_period, color='red', linestyle='--', linewidth=2, 
                label=f'Средний период: {avg_period:.4f} с')
    plt.legend()
    
    print(f"\nСтатистика периодов измерений:")
    print(f"  Всего измерений: {len(time_values)}")
    print(f"  Периодов: {len(periods)}")
    print(f"  Средний период: {avg_period:.4f} с")
    print(f"  Минимальный период: {min(periods):.4f} с")
    print(f"  Максимальный период: {max(periods):.4f} с")
    print(f"  Разброс: {max(periods) - min(periods):.4f} с")

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
        plot_sampling_period_hist(time_values)
        plt.show()
        
    except KeyboardInterrupt:
        print("\nИзмерения прерваны пользователем")
    finally:
        adc.deinit()