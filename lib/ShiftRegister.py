import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class ShiftRegister():

	def __init__(self, dataPin, clockPin, clearPin):
		print("ShiftRegister.__init__")
		self.dataPin = dataPin,
		self.clockPin = clockPin
		self.clearPin = clearPin

		self.setupBoard()

	def setupBoard(self):
		print("ShiftRegister.setupBoard")
		print("dataPin: %s" % self.dataPin)
		GPIO.setup(self.dataPin, GPIO.OUT)
		GPIO.output(self.dataPin, GPIO.LOW)

		print("clockPin: %s" % self.clockPin)
		GPIO.setup(self.clockPin, GPIO.OUT)
		GPIO.output(self.clockPin, GPIO.LOW)

		print("clearPin: %s" % self.clearPin)
		GPIO.setup(self.clearPin, GPIO.OUT)
		GPIO.output(self.clearPin, GPIO.LOW)

	def setValue(self, value):
		print("setValue: %s" % value)
		self.tick()

	def tick(self):
		print("tick")
		GPIO.ouput(self.clockPin, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(self.clockPin, GPIO.LOW)
		time.sleep(0.2)
