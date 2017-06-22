import pyvisa
import time

# time from function                                        DONE
# way to connect with any power supply (not just address 6) DONE
# connect to any channel                                    DONE
# set the voltage                                           DONE
# set the current                                           DONE
# measure voltage                                           DONE
# measure current                                           DONE
# turn on                                                   DONE
# turn off                                                  DONE

class Tektronix_PS2521G(object):
    
    # Initialization
    def __init__(self, num, ch):
        rm = pyvisa.ResourceManager()
        self.tektronix = rm.open_resource('GPIB0::' + str(num) + '::INSTR')
        self.tektronix.write("INST:NSEL " + str(ch))
        print("Connected to: " + self.tektronix.query("*IDN?\r"))
    
    # Measures current outputted by supply
    def measure_current(self, iterations, pause):
        current_readings = []
        for i in range(iterations):
            print("Current (A): " + (self.tektronix.query("MEAS:CURR?")))
            current_readings.append(self.tektronix.query("MEAS:CURR?"))
            time.sleep(pause)
            
    # Measures voltage outputted by supply
    def measure_voltage(self, iterations, pause):
        voltage_readings = []
        for i in range(iterations, pause):
            print("Voltage (V): " + (self.tektronix.query("MEAS:VOLT?")))
            voltage_readings.append(self.tektronix.query("MEAS:VOLT?"))
            time.sleep(pause)
        
    # Sets current of supply
    def set_current(self, desired_current):
        self.tektronix.write("CLS\r")
        self.tektronix.write("SOUR:CURR " + str(desired_current))
        print("New current: " + self.tektronix.query("SOUR:CURR?"))    
        
    # Sets voltage of supply
    def set_voltage(self, desired_voltage):
        self.tektronix.write("CLS\r")
        self.tektronix.write("SOUR:VOLT " + str(desired_voltage))
        print("New voltage: " + self.tektronix.query("SOUR:VOLT?"))
        
   
    # Powers on the supply
    def power_on(self):
        self.tektronix.write("CLS\r")
        self.tektronix.write("OUTP:STAT ON\r")
        print("Output status: " + self.tektronix.query("OUTP:STAT?"))
    
    # Powers off the supply    
    def power_off(self):
        self.tektronix.write("CLS\r")
        self.tektronix.write("OUTP:STAT OFF\r")
        print("Output status: " + self.tektronix.query("OUTP:STAT?"))
        
if __name__ == '__main__' :
    power_supply = Tektronix_PS2521G(6, 1)
    power_supply.set_voltage(1)
    power_supply.power_on()
    power_supply.measure_current(3,3)
    power_supply.power_off()
