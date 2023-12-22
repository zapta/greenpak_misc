Dec 2023. 

EDIT: Per http://tinyurl.com/arduino-pico-zadig, on Windows use Zadig to set “RP2 Boot2 (Interface 1)”
“WinUSB”, while the Pico is in boot mode (power on with button pressed). Alternativly install the Arduino
drivers as described below.


This windows driver was downloaded from https://github.com/arduino/ArduinoCore-mbed/tree/2.0.0/drivers
and it solved the automatic upload issue with the Arduino framework. Platformio also provide these 
drivers at ~/.platformio/packages/framework-arduino-mbed/drivers.


Installation method 1 
1. Connect the RPI Pico with the button pressed to enter the upload mode.

2. In the window device manager update the RP2 Boot device by selecting this directory
   as the location of the driver. This will use the following two files as driver
   *  nanorp2040connect.cat
   * nanorp2040connect.inf

Installation method 2
Run the dpinst-*.exe from https://github.com/arduino/ArduinoCore-mbed/tree/2.0.0/drivers
that is approriate to your sys tem.

Installation method 3
Install the arduino IDE and install from the Board Manager 'Arduino Mbed OS Nano Boards by Arduino'.
Note that as of Dec 2023, installing from the Board Manager Arduino MBed OS RP2040 by Arduino' doesn't install these drivers.  


