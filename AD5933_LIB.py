#include "libraries/Wire/Wire.h"
#include "libraries/ArduinoOTA/"

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
    def __init__(self, ADDR):
        self.address = ADDR

        # Reset the board
        def reset(void):
            pass

        # Temperature measuring
        def enableTemperature():
            pass
        def getTemperature():
            pass
        # Clock
        def setClockSource(byte):
            pass
        def setInternalClock(bool):
            pass
        def setSettlingCycles(int):
            pass
        # Frequency sweep configuration
        def setStartFrequency(freq):
            pass
        def setIncrementFrequency(inc):
            pass
        def setNumberIncrements(num):
            pass
        # Gain configuration
        def setPGAGain():
            pass
        # Excitation range configuration
        def setRange(range):
            pass

        # Read registers
        def readRegister():
            pass

        def readStatusRegister():
            pass
        def readControlRegister():
            pass
        # Impedance data
        def getComplexData(thing1m, thing2):
            pass
        # Set control mode register (CTRL_REG1)
        def setControlMode():
            pass
        # Power mode
        def setPowerMode():
            pass
        # Perform frequency sweeps
        def frequencySweep(real, imag):
            pass
        def calibrate(gain, phase, ref, n):
            pass

        def calibrate(gain, phase, real, imag, ref, n):
            pass


        # Private data
        self.clockSpeed = 16776000
        # Sending/Receiving byte method, for easy re-use
        def getByte():
            #not sure if needed
            pass
        def sendByte():
            # not sure if needed
            pass


    """
    {
    public:
        # Reset the board
        static bool reset(void);

        # Temperature measuring
        static bool enableTemperature(byte);
        static double getTemperature(void);

        # Clock
        static bool setClockSource(byte);
        static bool setInternalClock(bool);
        //bool setSettlingCycles(int); // not implemented - not used yet

        # Frequency sweep configuration
        static bool setStartFrequency(unsigned long);
        static bool setIncrementFrequency(unsigned long);
        static bool setNumberIncrements(unsigned int);

        # Gain configuration
        static bool setPGAGain(byte);

        # Excitation range configuration
        //bool setRange(byte, int); // not implemented - not used yet

        # Read registers
        static byte readRegister(byte);
        static byte readStatusRegister(void);
        static int readControlRegister(void);

        # Impedance data
        static bool getComplexData(int*, int*);

        # Set control mode register (CTRL_REG1)
        static bool setControlMode(byte);

        # Power mode
        static bool setPowerMode(byte);

        # Perform frequency sweeps
        static bool frequencySweep(int real[], int imag[], int);
        static bool calibrate(double gain[], int phase[], int ref, int n);
        static bool calibrate(double gain[], int phase[], int real[],
                              int imag[], int ref, int n);
    private:
        # Private data
        static const unsigned long clockSpeed = 16776000;

        # Sending/Receiving byte method, for easy re-use
        static int getByte(byte, byte*);
        static bool sendByte(byte, byte);
};
    
    """
