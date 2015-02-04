#! /usr/bin/python2.7
# -*-  coding: utf-8 -*-
__author__ = 'ovnislash'

def toMorse(message):
    morse = ""
    for car in message:
        if car == " ":
            morse = morse +"^" + " "
        else:
            morse = morse + codeMorse[corespondance.index(car)] + " "
    return morse

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
	"----"      #9
]

corespondance = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.0123456789"