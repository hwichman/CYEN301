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
#   Assignment 4 - Chat(timing) Covert Channel
#   Git Repo: https://github.com/hwichman/CYEN301/
#
##########################################################################

#Chat(timing)

import socket
import time
import sys
from binascii import hexlify
from time import time


#using constants
ZERO = 0.025
ONE = 0.1

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #create a socket
    print ("socket sucessfully created")

except socket.error as err:
    print ("socket creation failed with with error %s" %(err))


#ip = '138.47.148.167'
ip='jeangourd.com'
port = 1337

s.connect((ip,port))    #connect serve on some ip and port
s.bind(("", port))      #bind the socket to port 1337
s.listen(0)     #listen to connections

c,addr = s.accept()
print(c)

msg = "Some message..."     #send message one character at a time
n = 0
for i in msg:
    c.send(i)   #delay in between characters
    if (covert_bin[n] == "0"):
        time.sleep(ZERO)
    else:
        time.sleep(ONE)
    n = (n + 1) % len(covert_bin)

c.send("EOF")
c.close()

#convert transmittion to binary
covert = "secret" + "EOF"
covert_bin = ""

#receive data until the string "EOF"
t0 = time()
data = s.recv(4096)
t1 = time()
delta = round(t1 - t0, 3)
if (delta >= ONE):
    covert_bin += "1"
else:
    covert_bin += "0"

while (data.rstrip("\n") != "EOF"):
    sys.stdout.write(data)
    sys.stdout.flush()
s.close()

for i in covert:
    # convert each character to a full byte
    # hexlify converts ASCII to hex
    # int converts the hex to a decimal integer
    # bin provides its binary representation (with a 0b
    # prefix that must be removed)
    # that's the [2:] (return the string from the third
    # character on)
    # zfill left-pads the bit string with 0s to ensure a
    # full byte
    
    covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)

covert = ""
i = 0
while (i < len(covert_bin)):
    #process one byte at a time
    b = covert_bin[i:i + 8]
    #covert it to ASCII
    n = int("0b{}".format(b), 2)
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeErorr:
        covert += "?"
    # stop at the string "EOF"
    i += 8















