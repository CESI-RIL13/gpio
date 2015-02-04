#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import time
from morse import *
import wiringpi2 as wpi
wpi.wiringPiSetup()

PIN = 0
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
    while 1:
        myInput = wpi.digitalRead(PIN)
        debut = datetime.now()

        if(myInput):
            while myInput == 1:
                myInput = wpi.digitalRead(PIN)

            temps = datetime.now() - debut

            if(temps.seconds < 0.5):
                car = car + '.'
            else:
                car = car + '-'

        else:
            while myInput == 0:
                myInput = wpi.digitalRead(PIN)

                temps = datetime.now() - debut

                if(temps.seconds > 1 and car != ''):
                    return fromMorse(car)


# phrase = 'hello world'
#
# for car in phrase:
#     clignoteLED(toMorse(car.upper()))

phrase = ''
while 1:
    try:
        phrase = phrase + writeMorseCode()
    except KeyboardInterrupt:
        print phrase
