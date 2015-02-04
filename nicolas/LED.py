#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from morse import *
import wiringpi2 as wpi
wpi.wiringPiSetup()

def clignoteLED(phrase):
    for car in toMorse(phrase):
        if(car == '.'):
            wpi.digitalWrite(7, 1)
            time.sleep(0.25)
        elif(car == '-'):
            wpi.digitalWrite(7, 1)
            time.sleep(1)
        else:
            time.sleep(2)

        wpi.digitalWrite(7, 0)
        time.sleep(0.5)

phrase = 'hello world'
for car in phrase:
    clignoteLED(phrase.upper())
