#!/usr/bin/env python
"""v.1.0 """

import RPi.GPIO as GPIO
import time

#enable = 
pinA1 = 4
pinA2 = 17
pinB1 = 23
pinB2 = 24

#GPIO.setup(enable, GPIO.OUT)
GPIO.setup(pinA1, GPIO.OUT)
GPIO.setup(pinA2, GPIO.OUT)
GPIO.setup(pinB1, GPIO.OUT)
GPIO.setup(pinB2, GPIO.OUT)

GPIO.output(enable, 1)

def forward(delay, stepf):
    for s in range(0, stepf):
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)

def backward(delay, stepsb):
    for s in range(0, stepb):
        setStep(1, 0, 0, 1)
	time.sleep(delay)
	setStep(0, 1, 0, 1)
	time.sleep(delay)
	setStep(0, 1, 1, 0)
	time.sleep(delay)
	setStep(1, 0, 1, 0)
	time.sleep(delay)

def setStep(w1, w2, w3, w4):
    GPIO.output(pinA1, w1)
    GPIO.output(pinA2, w2)
    GPIO.output(pinB1, w3)
    GPIO.output(pinB2, w4)

while True:
    delay = raw_input("delay between steps (ms)")
    stepf = raw_input("steps forward?")
    stepb = raw_input("steps backward?")
    forward(delay, stepf)
    backward(delay, stepb)
