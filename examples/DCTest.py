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
myMotor = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(150)
myMotor2.setSpeed(150)
myMotor3.setSpeed(150)
myMotor.run(Adafruit_MotorHAT.FORWARD);
myMotor2.run(Adafruit_MotorHAT.FORWARD);
myMotor3.run(Adafruit_MotorHAT.FORWARD);
# turn on motor
myMotor.run(Adafruit_MotorHAT.RELEASE);
myMotor2.run(Adafruit_MotorHAT.RELEASE);
myMotor3.run(Adafruit_MotorHAT.RELEASE);

rng = 16
tm = 0.80

while (True):
	print "Forward! "
	myMotor.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
	myMotor3.run(Adafruit_MotorHAT.FORWARD)
#	time.sleep(0.5)	

#	myMotor.run(Adafruit_MotorHAT.BACKWARD)
#	myMotor2.run(Adafruit_MotorHAT.FORWARD)
#	time.sleep(0.5)	

	print "\tSpeed up..."
	for i in range(rng):
		myMotor.setSpeed(i**2)
		myMotor2.setSpeed(i**2)
		myMotor3.setSpeed(i**2)
		time.sleep(tm)

	print "\tSlow down..."
	for i in reversed(range(rng)):
		myMotor.setSpeed(i**2)
		myMotor2.setSpeed(i**2)
		myMotor3.setSpeed(i**2)
		time.sleep(tm)

	print "Backward! "
	myMotor.run(Adafruit_MotorHAT.BACKWARD)

	print "\tSpeed up..."
	for i in range(rng):
		myMotor.setSpeed(i**2)
		myMotor2.setSpeed(i**2)
		myMotor3.setSpeed(i**2)
		time.sleep(tm)

	print "\tSlow down..."
	for i in reversed(range(rng)):
		myMotor.setSpeed(i**2)
		myMotor2.setSpeed(i**2)
		myMotor3.setSpeed(i**2)
		time.sleep(tm)

	print "Release"
	myMotor.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	myMotor3.run(Adafruit_MotorHAT.RELEASE)

	time.sleep(0.01)
