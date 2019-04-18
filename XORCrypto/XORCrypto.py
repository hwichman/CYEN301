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
import binascii
k = "test"
m = "this"


def xor(text,key):
    xorMsg = ""
    i = 0
    for char in text:
        xorMsg += chr(ord(char) ^ ord(key[i]))
        i+=1                     
    return xorMsg

        

c = xor(m,k)
print (c)
new = xor(c,k)
print (new)
