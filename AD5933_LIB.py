#include "libraries/Wire/Wire.h"
#include "libraries/ArduinoOTA/"
import smbus
import time


# AD5933 Register Map
#Datasheet p23
#Device address and address pointer
AD5933_ADDR=0x0D
ADDR_PTR=0xB0
#Control Register
CTRL_REG1=0x80
CTRL_REG2=0x81
#Start Frequency Register
START_FREQ_1=0x82
START_FREQ_2=0x83
START_FREQ_3=0x84
#Frequency increment register
INC_FREQ_1=0x85
INC_FREQ_2=0x86
INC_FREQ_3=0x87
#Number of increments register
NUM_INC_1=0x88
NUM_INC_2=0x89
#Number of settling time cycles register
NUM_SCYCLES_1=0x8A
NUM_SCYCLES_2=0x8B
#Status register
STATUS_REG=0x8F
#Temperature data register
TEMP_DATA_1=0x92
TEMP_DATA_2=0x93
# Real data register
REAL_DATA_1=0x94
REAL_DATA_2=0x95
#Imaginary data register
IMAG_DATA_1=0x96
IMAG_DATA_2=0x97

#Constants
#Constants for use with the AD5933 library class.
#Temperature measuring

#define TEMP_MEASURE    (CTRL_TEMP_MEASURE)
#define TEMP_NO_MEASURE (CTRL_NO_OPERATION)

# ---------------- Clock sources ------------------------
#define CLOCK_INTERNAL  (CTRL_CLOCK_INTERNAL)
#define CLOCK_EXTERNAL  (CTRL_CLOCK_EXTERNAL)

# ---------------- PGA gain options ------------------------
#define PGA_GAIN_X1     (CTRL_PGA_GAIN_X1)
#define PGA_GAIN_X5     (CTRL_PGA_GAIN_X5)

# ---------------- Power modes ------------------------
#define POWER_STANDBY   (CTRL_STANDBY_MODE)
#define POWER_DOWN      (CTRL_POWER_DOWN_MODE)
#define POWER_ON        (CTRL_NO_OPERATION)

# ---------------- I2C result success/fail ------------------------
I2C_RESULT_SUCCESS = 0
I2C_RESULT_DATA_TOO_LONG = 1
I2C_RESULT_ADDR_NAK = 2
I2C_RESULT_DATA_NAK = 3
I2C_RESULT_OTHER_FAIL = 4

#Control register options
CTRL_NO_OPERATION = 0b00000000
CTRL_INIT_START_FREQ = 0b00010000
CTRL_START_FREQ_SWEEP = 0b00100000
CTRL_INCREMENT_FREQ = 0b00110000
CTRL_REPEAT_FREQ = 0b01000000
CTRL_TEMP_MEASURE = 0b10010000
CTRL_POWER_DOWN_MODE = 0b10100000
CTRL_STANDBY_MODE = 0b10110000
CTRL_RESET = 0b00010000
CTRL_CLOCK_EXTERNAL = 0b00001000
CTRL_CLOCK_INTERNAL = 0b00000000
CTRL_PGA_GAIN_X1 = 0b00000001
CTRL_PGA_GAIN_X5 = 0b00000000

#Status register options
STATUS_TEMP_VALID = 0x01
STATUS_DATA_VALID = 0x02
STATUS_SWEEP_DONE = 0x04
STATUS_ERROR = 0xFF

#Frequency sweep parameters
SWEEP_DELAY = 1

 #AD5933 Library class
 #Contains mainly functions for interfacing with the AD5933.

class AD5933:
    def __init__(self, ADDR, I2C_CHN):
        self.address = ADDR
        self.i2c_channel = I2C_CHN

        # Private data
        self._clockSpeed = 16776000

    # Reset the board
    def reset(void):
        pass
    def read_register(self, register):
        """
        Access i2c addres and extract register data
        :return: ???
        """
        bus = smbus.SMBus(self.i2c_channel)

        try:
            return bus.read_byte_data(self.address, register)
        except IOError:
            print("AD5933 Read Error. Add: %s Reg: %s", str(self.address), str(register))
        bus.close()

    def read_register2(self, register):
        """
        Access i2c addres and extract register data
        :return: ???
        """
        bus = smbus.SMBus(self.i2c_channel)

        try:
            temp_data = bus.read_byte_data(self.address, register)
            print("Successful read:  Addr: %s Reg: %s", str(self.address), str(register))
            return temp_data
           
        except IOError:
            print("AD5933 Read Error. Addr: %s Reg: %s", str(self.address), str(register))
        bus.close()
        
    # Temperature measuring
    def enableTemperature(self):
        pass
    def getTemperature(self):
        pass
    # Clock
    def setClockSource(self, byte):
        pass
    def setInternalClock(self, bool):
        pass
    def setSettlingCycles(self, int):
        pass
    # Frequency sweep configuration
    def setStartFrequency(self, freq):
        pass
    def setIncrementFrequency(self, inc):
        pass
    def setNumberIncrements(self, num):
        pass
    # Gain configuration
    def setPGAGain(self):
        pass
    # Excitation range configuration
    def setRange(self, range):
        pass

    # Read registers
    def readRegister(self):
        pass

    def readStatusRegister(self):
        pass
    def readControlRegister(self):
        pass
    # Impedance data
    def getComplexData(self, thing1m, thing2):
        pass
    # Set control mode register (CTRL_REG1)
    def setControlMode(self):
        pass
    # Power mode
    def setPowerMode(self):
        pass
    # Perform frequency sweeps
    def frequencySweep(self, real, imag):
        pass
    def calibrate(self, gain, phase, ref, n):
        pass

    def calibrate(self, gain, phase, real, imag, ref, n):
        pass


    # Sending/Receiving byte method, for easy re-use
    def getByte():
        #not sure if needed
        pass
    def sendByte():
        # not sure if needed
        pass

    # Misc useful functions
    def print_read(self, register):
        self.read_register(register)

if __name__ == "__main__":
    ad5933 = AD5933(AD5933_ADDR, 1)
    x1 = ad5933.read_register(TEMP_DATA_1)
    x2 = ad5933.read_register(TEMP_DATA_2)
    
    x1_2 = ad5933.read_register2(TEMP_DATA_1)
    x2_2 = ad5933.read_register2(TEMP_DATA_2)
    
    print("Temperature data:")
    print("X1: %d | X2: %d", x1, x2)
    time.sleep(0.5)
    print("done")
    
    print("Temperature data:")
    print("X1: %d | X2: %d", x1_2, x2_2)
    time.sleep(0.5)
    print("done")
