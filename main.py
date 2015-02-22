from lib.ShiftRegister import ShiftRegister
import time

dataPin  = 24
clockPin = 23
latchPin = 26

shiftRegister = ShiftRegister(dataPin, clockPin, latchPin)
shiftRegister.setValue(0)
time.sleep(1)
shiftRegister.setValue(1)
time.sleep(1)
shiftRegister.setValue(0)
time.sleep(1)
shiftRegister.setValue(1)
time.sleep(1)
shiftRegister.setValue(0)
time.sleep(1)
shiftRegister.setValue(1)
time.sleep(1)
shiftRegister.setValue(0)
time.sleep(1)
shiftRegister.setValue(1)
time.sleep(1)