#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit


# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
myMotor = mh.getMotor(3)
myMotor2 = mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(150)
myMotor2.setSpeed(150)
myMotor.run(Adafruit_MotorHAT.FORWARD);
myMotor2.run(Adafruit_MotorHAT.FORWARD);
# turn on motor
myMotor.run(Adafruit_MotorHAT.RELEASE);

rng = 16
time = 1

while (True):
	print "Forward! "
	myMotor.run(Adafruit_MotorHAT.FORWARD)
#	myMotor2.run(Adafruit_MotorHAT.BACKWARD)
#	time.sleep(0.5)	

#	myMotor.run(Adafruit_MotorHAT.BACKWARD)
#	myMotor2.run(Adafruit_MotorHAT.FORWARD)
#	time.sleep(0.5)	

	print "\tSpeed up..."
	for i in range(rng):
		myMotor.setSpeed(i**2)
		time.sleep(time)

	print "\tSlow down..."
	for i in reversed(range(rng)):
		myMotor.setSpeed(i**2)
		time.sleep(time)

	print "Backward! "
	myMotor.run(Adafruit_MotorHAT.BACKWARD)

	print "\tSpeed up..."
	for i in range(rng):
		myMotor.setSpeed(i**2)
		time.sleep(time)

	print "\tSlow down..."
	for i in reversed(range(rng)):
		myMotor.setSpeed(i**2)
		time.sleep(time)

	print "Release"
	myMotor.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(0.01)
