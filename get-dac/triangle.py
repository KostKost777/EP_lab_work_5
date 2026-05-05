from r2r_dac import R2R_DAC
from pwm_dac import PWM_DAC
from mcp4725_driver import MCP4725
import time as t
import signal_generator as sg

# DAC = R2R_DAC
# DAC = PWM_DAC
DAC = MCP4725

amplitude = 1
signal_frequency = 20
sampling_frequency = 100

def main():
    dac = DAC(verbose=False)

    while True:
        try:
            time = t.time_ns()/10e9
            voltage = sg.get_triange_wave_amplitude(signal_frequency, time) * amplitude
            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)
        except KeyboardInterrupt:
            print("CTRL + c intercepted, exiting")
            dac.deinit()
            break

if __name__ == "__main__":
    main()