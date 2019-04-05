##########################################################################
#
#   Team: Incas
#
#   Members:    Matt LaCroix
#               Ben Doughty, btd001@latech.edu
#               Stella Li
#               Seth Martin
#               Haley Wichman
#               Richard Rose
#               Bibhut Khadka
#
#   Assignment 2 - FTP (storage) Covert Channel
#   Git Repo: https://github.com/hwichman/CYEN301/
#
##########################################################################

#FTP Covert Channel Decoder

import ftplib

#allows you to use methods "7" or "10" to decode the FTP covert channel
#method "7" - skips files/folders where the first 3 permission bits are not "---"
# this method also decodes using 7-bit groupings only
#method "10" - uses all 10 permission bits; this uses all files/folders and concatenates all files in a directory
# method may be encoded in 7-bit or 8-bit groupings, so both decoding methods are tried
METHOD = 10

#decoder
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

#connects to ftp server
ftp = ftplib.FTP('jeangourd.com','anonymous','')

#empty list to contain strings of file information
files = []

#adds file information of each file to array
ftp.dir(files.append)

#truncates file information to first 10 characters each
for index in range(len(files)):
    files[index] = files[index][:10]

#"files" now contains permission strings for every file in the directory
#builds a single string which will be fed into the decoder
covertmessage = ""
for permission in files:
    if (METHOD == 10) or (permission[:3] == "---"):
        for letter in permission:
            if (letter == "-"):
                covertmessage += '0'
            else:
                covertmessage += '1'

#main
print("Permissions: ", files)
print("Binary-Encoded Message: ", covertmessage)
print("Decoded Message: ")
if (METHOD == 7):
    print(decode(7,covertmessage))
else:
    print(decode(7, covertmessage))
    print(decode(8, covertmessage))





