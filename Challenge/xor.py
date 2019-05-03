#!/usr/bin/env python
##########################################################################
#
#   Team: Incas
#
#   Members:    Matt LaCroix
#               Ben Doughty, btd001@latech.edu
#               Stella Li
#               Seth Martin
#               Haley Wichman, hrw010@latech.edu
#               Richard Rose
#               Bibhut Khadka
#
#   Assignment 6 - XOR Crypto
#   Git Repo: https://github.com/hwichman/CYEN301/
#
##########################################################################

#XOR Crypto
import sys

keyfile = open("key","r")

#takes the text parameter and xors it with the key parameter and returns the result
def xor(text,key):
    xorMsg = ""
    i = 0
    for char in text:
        xorMsg += chr(ord(char) ^ ord(key[i]))
        i+=1                     
    return xorMsg

#read input from stdin
inData = ""
for line in sys.stdin:
	inData += line

#read input from "key" file in the current directory
keyData= ""
for line in keyfile:
	keyData += line

#write the xor'd output to stdout
sys.stdout.write(xor(inData, keyData))

	
