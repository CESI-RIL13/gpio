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

#todo
#entree

pin = 0
debut = 0
fin = 0
stop = 0
morse = ''
record = ''

def writeLetter(morse,record):
    if morse == '':
        record = record+' '
    else :
        record = record+corespondance[codeMorse.find(morse)]
    stop = 0
    morse = ''
    print record

def writeMorse(morse,d,f):
    if (f-d)>1:
        morse = morse+"-"
    else:
        morse = morse+"."
    debut = 0
    fin = 0
    stop = 0

i=0
while(i==0):
    if(wpi.digitalRead(pin) == 1):
        if debut == 0:
            debut = time.clock()
    else :
        if debut != 0:
            fin = time.clock()
            writeMorse(morse,debut,fin)
        elif stop == 0:
            stop = time.clock()
        else:
            if stop-time.clock() > 2:
                writeLetter(morse,record)
    #wpi.digitalRead(pin)

