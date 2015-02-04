#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from morse import *
import wiringpi2 as wpi
wpi.wiringPiSetup()

def clignoteCourt(pin):
    wpi.digitalWrite(pin, 1)
    time.sleep(1)

    wpi.digitalWrite(pin, 0)
    time.sleep(1)

def clignoteLong(pin):
    wpi.digitalWrite(pin, 1)
    time.sleep(2)

    wpi.digitalWrite(pin, 0)
    time.sleep(1)

def choixClignote(mot):
    for car in toMorse(mot):
        if(car <> ' '):
            if(car == '.'):
                clignoteCourt(7)
            else:
                clignoteLong(7)



mot = 'bonjour'
choixClignote(mot)