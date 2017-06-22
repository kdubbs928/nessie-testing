import pyvisa
import time

rm = pyvisa.ResourceManager()
#print(rm.list_resources())
tektronix = rm.open_resource('GPIB0::6::INSTR')

print("Connected to: " + tektronix.query("*IDN?\r"))

current_readings = []

for i in range(10):
    #time.sleep(30)

    print("Current (A): " + (tektronix.query("MEAS:CURR?")))
    current_readings.append(tektronix.query("MEAS:CURR?"))

    time.sleep(3)
