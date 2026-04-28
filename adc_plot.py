import matplotlib.pyplot as plt
import numpy as np

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.title("Зависимость напряжения на выходе ЦАП от времени")
    plt.xlabel("Время (с)")
    plt.ylabel("Напряжение (В)")
    plt.xlim(min(time), max(time))
    plt.ylim(0, max_voltage * 1.1)
    plt.grid(True)
    plt.savefig("voltage_vs_time.png")
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range(1, len(time)):
        period = time[i] - time[i-1]
        sampling_periods.append(period)
    
    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods, bins=20, edgecolor='black')
    plt.title("Распределение количества измерений по их продолжительности")
    plt.xlabel("Продолжительность измерения (с)")
    plt.ylabel("Количество измерений")
    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.savefig("sampling_period_hist.png")
    plt.show()