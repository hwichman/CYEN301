##########################################################################
#
#   Team: Incas
#
#   Members:    Matt LaCroix
#               Ben Doughty
#               Stella Li
#               Seth Martin
#               Haley Wichman
#               Richard
#
#   Assignment 1 - Binary Decoder
#
#   Git Repo: https://github.com/hwichman/CYEN301/
#
##########################################################################


#Binary Decoder
import sys
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
        if (n!=8 and n>0 and n<128):
            decodedMessage += chr(n)
    #return the resulting string
    return decodedMessage

#main
for line in stdin:
    sys.stdout.write(decode(7,line))
    sys.stdout.write(decode(8,line))
