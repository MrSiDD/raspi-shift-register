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
    startTime = time.time()
    period = 1
    delta = [x*0.33 for x in xrange(8)]
    tempLed = generateRandomLedState()

    while True:
        t = time.time() - startTime
        t = t/period

        for x in xrange(8):
            l = (t - delta[x]) % 2.0

            if (l >= 1):
                shiftRegister.setValue(tempLed)
            else:
                shiftRegister.setValue(nullLed)

except(SystemError, KeyboardInterrupt):
    print("Done!")
finally:
    shiftRegister.cleanup()