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

from socket import socket, AF_INET, SOCK_STREAM
from time import time
from sys import stdout
from threading import Thread
from binascii import unhexlify

def receive():
    covert_bin = ""
    while True:
        try:
            t0 = time()
            data = s.recv(BUFSIZ)
            t1 = time()
            if (data.rstrip("\n") == "EOF"):
                break
            delta = round(t1-t0,3)
            if (delta >= ONE):
                covert_bin += "1"
            else:
                covert_bin += "0"
            stdout.write(data)
            stdout.flush()
        except OSError:
            break
    covert = ""
    i = 0
    while (i < len(covert_bin)):
        # process one byte at a time
        b = covert_bin[i:i + 8]
        # convert it to ASCII
        n = int("0b{}".format(b), 2)
        try:
            covert += unhexlify("{0:x}".format(n))
        except TypeError:
            covert += "?"
        # stop at the string "EOF"
        i += 8
    stdout.write(covert)
    

#using constants
ZERO = 0.1
ONE = 0.025
HOST = 'jeangourd.com'
PORT = 31337
BUFSIZ = 4096

ADDR = (HOST,PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
