from lib.ShiftRegister import ShiftRegister
import time

dataPin  = 24
clockPin = 23
latchPin = 26

shiftRegister = ShiftRegister(dataPin, clockPin, latchPin)

try:
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

except(KeyboardInterrupt, SystemExit):
	print("Exit ...")

finally:
	GPIO.cleanup()