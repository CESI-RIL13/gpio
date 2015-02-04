#! /usr/bin/python2.7
# -*-  coding: utf-8 -*-
__author__ = 'ovnislash'

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
	"-...",     #6
	"--...",    #7
	"---..",    #8
	"----"      #9
]

corespondance = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.0123456789"

def toMorse(car):
    if car == ' ':
        return ''
    return codeMorse[corespondance.index(car)]

def fromMorse(code):
    return corespondance[codeMorse.index(code)]