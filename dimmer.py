import time,random,string
from lib.ShiftRegister import ShiftRegister

dataPin  = 14
clockPin = 18
latchPin = 15

shiftRegister = ShiftRegister(dataPin, clockPin, latchPin)

nullLed = [0,0,0,0,0,0,0,0]

def generateRandomLedState():
    led = []
    for i in range(0,8):
        led.append(random.randint(0,1))
    return led

try:
    while True:
        tempLed = generateRandomLedState()
        for i in range(0,10):
            shiftRegister.setValue(tempLed)
            time.sleep(0.001 * i)
            shiftRegister.setValue(nullLed)
            time.sleep(0.001 * i)

        for i in reversed(range(0,10)):
            shiftRegister.setValue(tempLed)
            time.sleep(0.001 * i)
            shiftRegister.setValue(nullLed)
            time.sleep(0.001 * i)

except(SystemError, KeyboardInterrupt):
    print("Done!")