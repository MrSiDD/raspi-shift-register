# raspi-shift-register

Basic functionality to use a shift register with a raspi.
This project is work in progress.

Usage: 
```
from lib.ShiftRegister import ShiftRegister

dataPin  = 24
clockPin = 23
clearPin = 26

shiftRegister = ShiftRegister(dataPin, clockPin, clearPin)
```