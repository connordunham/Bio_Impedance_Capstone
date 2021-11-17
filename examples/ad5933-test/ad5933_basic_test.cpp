// Author: Connor Dunham
// Date: November 17, 2021
// Purpose of this code is to execute a basic CPP program that can acheive the following:
//    1. Access I2C pins on rasberry pi
//    2. Read and write to AD5933
//    3. Perform measurements with AD5933


#include <Wire.h>
#include "AD5933.h"

#include <iostream>
#include <errno.h>
#include <wiringPiSPI.h>
#include <unistd.h>

using namespace std;
// channel is the wiringPi name for the chip select (or chip enable) pin.
// Set this to 0 or 1, depending on how it's connected.




#define START_FREQ  (80000)
#define FREQ_INCR   (1000)
#define NUM_INCR    (40)
#define REF_RESIST  (10000)

static const int CHANNEL = 1;
static const double gain[NUM_INCR+1];
static const int phase[NUM_INCR+1];


void setup
{
}


void main
{

    // ------------------ SETUP ------------------------
    
    int fd, result;
    cout << "Initializing" << endl ;
    
    
    // Configure the interface.
    // CHANNEL insicates chip select,
    // 500000 indicates bus speed.
    fd = wiringPiSPISetup(CHANNEL, 500000);
    cout << "Init result: " << fd << endl;

    int fd, result;
     
    cout << "Initializing" << endl ;
    // Configure the interface.
    // CHANNEL insicates chip select,
    // 500000 indicates bus speed.
    fd = wiringPiSPISetup(CHANNEL, 500000);
    cout << "Init result: " << fd << endl;
    
    
    // ------------------ MAIN ---------------------
    
}
