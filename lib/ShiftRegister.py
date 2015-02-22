import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class ShiftRegister():

	def __init__(self, dataPin, clockPin, latchPin):
		print("ShiftRegister.__init__")
		self.dataPin = dataPin,
		self.clockPin = clockPin
		self.latchPin = latchPin

		self.setupBoard()

	def setupBoard(self):
		print("ShiftRegister.setupBoard")
		print("dataPin: %s" % self.dataPin)
		GPIO.setup(self.dataPin, GPIO.OUT)
		GPIO.output(self.dataPin, GPIO.LOW)

		print("clockPin: %s" % self.clockPin)
		GPIO.setup(self.clockPin, GPIO.OUT)
		GPIO.output(self.clockPin, GPIO.LOW)

		print("latchPin: %s" % self.latchPin)
		GPIO.setup(self.latchPin, GPIO.OUT)
		GPIO.output(self.latchPin, GPIO.LOW)

	def setValue(self, value):
		print("setValue: %s" % value)
		for i in value:
			if (value[i] > 0):
				GPIO.output(self.dataPin, GPIO.HIGH)
			else:
				GPIO.output(self.dataPin, GPIO.LOW)
			self.tick()

		self.writeOut(self)

	def writeOut(self):
		print("writeOut")
		GPIO.output(self.latchPin, GPIO.LOW)
		time.sleep(0.2)
		GPIO.OUTPUT(self.latchPin, GPIO.HIGH)
		time.sleep(0.2)

	def tick(self):
		print("tick")
		GPIO.ouput(self.clockPin, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(self.clockPin, GPIO.LOW)
		time.sleep(0.2)
