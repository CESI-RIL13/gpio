#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from morse import *
import wiringpi2 as wpi
wpi.wiringPiSetup()

PIN = 7
LED_SHORT = 0.25
LED_LONG = 1
MOT = 2
CARACTERE = 0.5

def clignoteLED(morseCar):
    for car in morseCar:
        if(car == '.'):
            wpi.digitalWrite(PIN, 1)
            time.sleep(LED_SHORT)
        elif(car == '-'):
            wpi.digitalWrite(PIN, 1)
            time.sleep(LED_LONG)
        else:
            time.sleep(MOT)

        wpi.digitalWrite(PIN, 0)
        time.sleep(CARACTERE)


def writeMorseCode():
    car =''
    if wpi.digitalRead(PIN):
        print "je lis le pin %d" %PIN


# phrase = 'hello world'
#
# for car in phrase:
#     clignoteLED(toMorse(car.upper()))

while 1:
    try:
        writeMorseCode()
    except KeyboardInterrupt:
        print "salut!!"
