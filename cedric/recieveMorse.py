#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cedric'
import wiringpi2 as wpi
import morse
from datetime import datetime
from time import sleep, time
bouton=""
debut=datetime.now()
duree=""
code=""
PIN=0
wpi.wiringPiSetup()

# phrase = raw_input("taper du morse : ")
# phrase = phrase.split()
# retour=""
# for code in phrase:
#     retour = retour + morse.fromMorse(code)
#
# print retour

while(1):
    bouton=wpi.digitalRead(PIN)
    debut=datetime.now()
    if bouton == 1:
        while bouton == 1:
            bouton=wpi.digitalRead(PIN)
            sleep(0.02)
        duree=datetime.now()-debut
        if duree.seconds < 0.5:
            code += "."
        else:
            code += "-"
    else:
        while bouton == 0:
            bouton=wpi.digitalRead(PIN)
            sleep(0.02)
        duree=datetime.now()-debut
        if duree.seconds > 1:
            code += " "
        elif duree.seconds >2:
            break

code = code.split()
retour = ""
for lettre in code:
    retour += morse.fromMorse(lettre)

print retour