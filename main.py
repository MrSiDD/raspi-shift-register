from lib.ShiftRegister import ShiftRegister
import time

dataPin  = 14
clockPin = 15
latchPin = 18

shiftRegister = ShiftRegister(dataPin, clockPin, latchPin)

led1 = [1,0,0,0,0,0,0]
led2 = [1,1,0,0,0,0,0]
led3 = [1,1,1,0,0,0,0]
led4 = [1,1,1,1,0,0,0]
led5 = [1,1,1,1,1,0,0]
led6 = [1,1,1,1,1,1,0]
led7 = [1,1,1,1,1,1,1]
led8 = [0,0,0,0,0,0,0]

try:
	shiftRegister.setValue(led1)
	time.sleep(1)
	shiftRegister.setValue(led2)
	time.sleep(1)
	shiftRegister.setValue(led3)
	time.sleep(1)
	shiftRegister.setValue(led4)
	time.sleep(1)
	shiftRegister.setValue(led5)
	time.sleep(1)
	shiftRegister.setValue(led6)
	time.sleep(1)
	shiftRegister.setValue(led7)
	time.sleep(1)
	shiftRegister.setValue(led8)

except(KeyboardInterrupt, SystemExit):
	print("Exit ...")

finally:
	shiftRegister.cleanup()
