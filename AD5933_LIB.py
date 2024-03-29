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
        self.debug = True

        # Private data
        self._clockSpeed = 16776000

    # Reset the board
    def reset(self):
        # Get the current valkue of the control register
        val = self.getByte(CTRL_REG2)

        if not val:
            return False
        # Set bit D4 for restart
        val = val | CTRL_RESET

        #Send byte back
        return self.sendByte(CTRL_REG2, val)

    def getByte(self, register):
        """
        Access i2c addres and extract register data
        :return: ???
        """
        bus = smbus.SMBus(self.i2c_channel)

        try:
            val = bus.read_byte_data(self.address, register)

            # Debug Data Visualization
            if(self.debug):
                print("AD5933 Read Success. Addres: ", hex(self.address), " Reg: ", hex(register), "Data:", hex(val))
            return val
          
        except IOError:
            print("AD5933 Read Error. Address: ", hex(self.address), " Reg: ", hex(register))
            return False

        bus.close()


    def sendByte(self, register, byte):
        bus = smbus.SMBus(self.i2c_channel)

        try:
            bus.write_byte_data(self.address, register, byte)

            # Debug Data Visualization
            if (self.debug):
                print("AD5933 Write Success. Address: ", hex(self.address), " Reg: ", hex(register), "Data:", hex(byte))

            return True

        except IOError:
            print("AD5933 Write Error. Address: ", hex(self.address), " Reg: ", hex(register), "Data:", hex(byte))
            return False

        bus.close()



    # Temperature measuring
    def enableTemperature(self):
        # Retrieve current control reg values
        #read_control_reg = self.readControlRegister()
        #write_control_reg = read_control_reg & CTRL_TEMP_MEASURE

        if(self.sendByte(CTRL_REG2, CTRL_TEMP_MEASURE)):
            self.verify_write(CTRL_REG2, CTRL_TEMP_MEASURE)
            print("Temperature Enabled")
        else:print("Temperature Failed")

        #elf.sendByte(CTRL_REG2, CTRL_NO_OPERATION)

    def getTemperature(self):
        """
        Positive Temperature = ADC Code (D)/32
        Negative Temperature = (ADC Code (D) – 16384)/32
        where ADC Code uses all 14 bits of the data byte, including the sign bit.
        Negative Temperature = (ADC Code (D) – 8192)/32
        where ADC Code (D) is D13, the sign bit, and is removed from the ADC code.)
        DIGITAL OUTPUT–40°C–0.03125°C–30°C11,1111,1111,111111,1100, 0100, 000011, 1011, 0000, 0000TEMPERATURE (°C)75°C150°C01, 0010,1100, 000000,
        :return:
        """
        # Set control reg byte for temp read
        self.enableTemperature()
        # Read bits D0 - D7 of temperature reg at TEMP_DATA_1 register
        temp1 = self.getByte(TEMP_DATA_1)
        # Shift
        temp1 = temp1 << 8
        # Read bits D8 - D15 of temperature reg at TEMP_DATA_2 register
        temp2 = self.getByte(TEMP_DATA_2)

        # Combine both register
        temp = temp1 | temp2
        if int(temp > 1000):
            deg = (temp - 16384)/32
        else:
            deg = temp/32

        status = self.readStatusRegister()
        if (self.readStatusRegister() & 0x1):
            print("Valid Temp Reading")
        else:
            print("Invalid Temp Reading:", bin(status))

        # Return device to no-operations
        self.sendByte(CTRL_REG2, CTRL_NO_OPERATION)

        print("temp1:", temp1)
        print("temp2:", temp2)
        print("temp:", temp)
        print("deg:", deg)
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
        return self.getByte(STATUS_REG)

    def readControlRegister(self):
        byte1 = self.getByte(CTRL_REG1)
        byte1 = byte1 << 8
        byte2 = self.getByte(CTRL_REG2)
        return byte2 | byte1


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

    def verify_write(self, register, value):
        byte = self.getByte(register)
        compare = value & byte
        print("write desired:", bin(value))
        print("current reg val:", bin(byte))

    # Misc useful functions
    def print_read(self, register):
        self.getByte(register)

if __name__ == "__main__":

    ad5933 = AD5933(AD5933_ADDR, 1)
    ad5933.sendByte(0x80, 0xff)

    if(ad5933.reset()):
        ad5933.getTemperature()
    else:print("reset fail")


    """
    Stable Register access functions
    
    while True:
        ad5933.sendByte(CTRL_REG2, CTRL_TEMP_MEASURE)

        print("\n\nTEMP WRITE")
        x = str(bin(ad5933.getByte(CTRL_REG2))) + str(bin(ad5933.getByte(CTRL_REG1)))
        print(x)



        print("\n\nSNTBY WRITE")
        ad5933.sendByte(CTRL_REG2, CTRL_STANDBY_MODE)

        x = str(bin(ad5933.getByte(CTRL_REG2))) + str(bin(ad5933.getByte(CTRL_REG1)))
        print(x)
        time.sleep(5)
    """


