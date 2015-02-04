#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cedric'
import wiringpi2 as wpi
import morse
from datetime import datetime
from time import sleep
bouton=""
debut=datetime.now()
duree=""
wpi.wiringPiSetup()

# phrase = raw_input("taper du morse : ")
# phrase = phrase.split()
# retour=""
# for code in phrase:
#     retour = retour + morse.fromMorse(code)
#
# print retour

while(1):
    bouton=wpi.digitalRead(7)
    if bouton == 1:
        debut=datetime.now()
        while bouton == 1:
            bouton=wpi.digitalRead(7)
            sleep(0.02)
        print datetime.now()-debut
