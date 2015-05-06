#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

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

################################# Motors
myMotor = mh.getMotor(1)
myMotor2 = mh.getMotor(2)


myStepper = mh.getStepper(200, 2)  	
myStepper.setSpeed(30)  		

myMotor.setSpeed(50)
myMotor2.setSpeed(50)


# turn on motor

myMotor.run(Adafruit_MotorHAT.FORWARD);
myMotor2.run(Adafruit_MotorHAT.FORWARD);


myMotor.run(Adafruit_MotorHAT.RELEASE);
myMotor2.run(Adafruit_MotorHAT.RELEASE);


while (True):
	print "sup"
	myMotor.run(Adafruit_MotorHAT.FORWARD)
	myMotor2.run(Adafruit_MotorHAT.FORWARD)
	myStepper.step(1000, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
	myStepper.step(1000, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
	print "guys"
	myMotor.run(Adafruit_MotorHAT.RELEASE)
	myMotor2.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(1.0)