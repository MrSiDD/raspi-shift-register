import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class ShiftRegister():

	def __init__(self, dataPin, clockPin, latchPin):
		self.dataPin = dataPin,
		self.clockPin = clockPin
		self.latchPin = latchPin

		self.setupBoard()

	def setupBoard(self):
		GPIO.setup(self.dataPin, GPIO.OUT)
		GPIO.output(self.dataPin, GPIO.LOW)

		GPIO.setup(self.clockPin, GPIO.OUT)
		GPIO.output(self.clockPin, GPIO.LOW)

		GPIO.setup(self.latchPin, GPIO.OUT)
		GPIO.output(self.latchPin, GPIO.LOW)

	def setValue(self, value):
		for i in value:
			if (i > 0):
				GPIO.output(self.dataPin, GPIO.HIGH)
			else:
				GPIO.output(self.dataPin, GPIO.LOW)
			self.tick()

		self.writeOut()

	def writeOut(self):
		GPIO.output(self.latchPin, GPIO.LOW)
		#time.sleep(0.2)
		GPIO.output(self.latchPin, GPIO.HIGH)
		#time.sleep(0.2)

	def tick(self):
		GPIO.output(self.clockPin, GPIO.HIGH)
		#time.sleep(0.2)
		GPIO.output(self.clockPin, GPIO.LOW)
		#time.sleep(0.2)

	def cleanup(self):
		GPIO.cleanup()
