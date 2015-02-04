#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from morse import *
import wiringpi2 as wpi
wpi.wiringPiSetup()

def clignoteLED(morseCar):
    for car in morseCar:
        convertCar = toMorse(car)
        if(convertCar == '.'):
            wpi.digitalWrite(7, 1)
            time.sleep(0.25)
        elif(convertCar == '-'):
            wpi.digitalWrite(7, 1)
            time.sleep(1)
        else:
            time.sleep(2)

        wpi.digitalWrite(7, 0)
        time.sleep(0.5)

phrase = 'hello world'

for car in phrase:
    clignoteLED(toMorse(car.upper()))