#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cedric'
import wiringpi2 as wpi
import morse
import time
from time import sleep
bouton=""
debut=time.time()
duree=""
PIN=0
wpi.wiringPiSetup()

while(1):
    bouton=wpi.digitalRead(PIN)
    if bouton == 1:
        debut=time.time()
        while bouton == 1:
            bouton=wpi.digitalRead(PIN)
            sleep(0.02)
        temps = time.time()-debut
	if(temps < 1):
		print "."
	else :
		print "_"
	