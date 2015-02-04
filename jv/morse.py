#! /usr/bin/python2.7
# -*-  coding: utf-8 -*-
__author__ = 'ovnislash'

import time
import wiringpi2 as wpi
wpi.wiringPiSetup()
#wpi.digitalRead(numéro de la pin)

codeMorse = [
 	".-",       #A
 	"-...",     #B
 	"-.-.",     #C
 	"-..",      #D
 	".",        #E
 	"..-.",     #F
 	"--.",      #G
 	"....",     #H
 	"..",       #I
	".---",     #J
	"-.-",      #K
	".-..",     #L
	"--",       #M
	"-.",       #N
	"---",      #O
	".--.",     #P
	"--.-",     #Q
	".-.",      #R
	"...",      #S
	"-",        #T
	"..-",      #U
	"...-",     #V
	".--",      #W
	"-..-",     #X
	"-.--",     #Y
	"--..",     #Z
	".-.-.-",   #.
	"-----",    #0
	".----",    #1
	"..---",    #2
	"...--",    #3
	"....-",    #4
	".....",    #5
	"-....",    #6
	"--...",    #7
	"---..",    #8
	"----",     #9
]

corespondance = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.0123456789"


def tradMorse(phrase):
    i = 0
    pin = 7
    phraseMorse = {}
    for letter in phrase:
        if letter == " ":
            phraseMorse[i] = "+"
        phraseMorse[i] = codeMorse[corespondance.find(letter)]
        i=i+1

    for letterMorse in phraseMorse.values():
        for impulsion in letterMorse:
            if impulsion == ".":
                wpi.digitalWrite(pin, 1)
                time.sleep(0.25)
                wpi.digitalWrite(pin, 0)
            elif impulsion == "-":
                wpi.digitalWrite(pin, 1)
                time.sleep(1.25)
                wpi.digitalWrite(pin, 0)
            elif impulsion == "+":
                time.sleep(2.25)
            time.sleep(0.75)
        time.sleep(1)

i = 0
while(i == 0) :
    phrase = raw_input('Phrase à traduire :')
    phrase = phrase.upper()
    tradMorse(phrase)

