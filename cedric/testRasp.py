#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cedric'
import wiringpi2 as wpi
import morse
from time import sleep

def long():
    wpi.digitalWrite(7,1)
    sleep(2)

def court():
    wpi.digitalWrite(7,1)
    sleep(1)

def espace():
    wpi.digitalWrite(7,0)
    sleep(3)

def interLettre():
    wpi.digitalWrite(7,0)
    sleep(.5)

def envoyerMorse(lettre):
    #lettre=""
    for car in lettre:
        #print car
        if car == ".":
            interLettre()
            court()
        elif car == "-":
            interLettre()
            long()
        elif car == "^":
            espace()
    sleep(2)


wpi.wiringPiSetup()

phrase = raw_input("Message à envoyer en morse : ")
phrase= phrase.upper()

code=morse.toMorse(phrase).split()

for lettre in code:
    envoyerMorse(lettre)

