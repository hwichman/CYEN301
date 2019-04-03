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
#   Assignment 2 - FTP (storage) Covert Channel
#   Git Repo: https://github.com/hwichman/CYEN301/
#
##########################################################################

#FTP Covert Channel Decoder

from ftplib import FTP
def METHOD(files):
    for line in files:
        if (line[:3] != "---"):
            return 10
    return 7

def decode(grouping,binaryString):
    #detect if it is an 8 bit or 7 bit
    #split the string into groups of "grouping", put data in an array
    #initialize a string array
    groupings = []
    i = 0
    currentBinaryString = ""
    for char in binaryString:
        if (i != 0 and i % grouping == 0):
            groupings.append(currentBinaryString)
            currentBinaryString = char
        elif (i == len(binaryString)-1):
            currentBinaryString += char
            groupings.append(currentBinaryString)
        else:
            currentBinaryString += char
        i += 1
    #convert each grouping into a character
    decodedMessage = ""
    for binaryGrouping in groupings:
        n = int(binaryGrouping,2)
        if (n == 8):
            decodedMessage = decodedMessage[:len(decodedMessage)-1]
        if (n!=8 and n>31 and n<128):
            decodedMessage += chr(n)
    #return the resulting string
    return decodedMessage


#The number of bits it reads in each line
MAX_READTYPE = 10
ftp = FTP('jeangourd.com','anonymous','')

files = []
ftp.dir(files.append)

#readType = METHOD(files)
readType = 7

charString = ""
if (readType <= MAX_READTYPE and readType > 0):
    for line in files:
        print (line)
        charString += line[10-readType:10]
else:
    print ("Invalid read type range: should be 0 to ", MAX_READTYPE)
print (charString)
binaryString = ""
for char in charString:
	if (char == '-'):
		binaryString += '0';
	else:
		binaryString += '1';
print (binaryString)
	
print (decode(7, binaryString))
print ("\n")
print (decode(8, binaryString))
print ("\n")
