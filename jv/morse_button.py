#! /usr/bin/python2.7
# -*-  coding: utf-8 -*-
__author__ = 'ovnislash'

import time
import wiringpi2 as wpi
wpi.wiringPiSetup()

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

class MorseDecoder(object):
    def __init__(self):
        self.debut = 0
        self.fin = 0
        self.stop = 0
        self.morse = ''
        self.record = ''

    def writeLetter(self):
        if self.morse == '':
            self.record = self.record+' '
        else :
            self.record = self.record+corespondance[codeMorse.find(self.morse)]
        self.stop = 0
        self.morse = ''
        print self.record

    def writeMorse(self):
        if (self.fin-self.debut)>1:
            self.morse = self.morse+"-"
        else:
            self.morse = self.morse+"."
        self.debut = 0
        self.fin = 0
        self.stop = 0

md = MorseDecoder()

i=0
pin=0
while(i==0):
    if wpi.digitalRead(pin) == 1:
        if md.debut == 0:
            md.debut = time.clock()
    else :
        if md.debut != 0:
            md.fin = time.clock()
            md. writeMorse()
        elif md.stop == 0:
            md.stop = time.clock()
        else:
            if time.clock()-md.stop > 2:
                md.writeLetter()
    time.sleep(0.1)