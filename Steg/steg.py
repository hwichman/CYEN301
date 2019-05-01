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
#   Assignment 7 - Steg
#   Git Repo: https://github.com/hwichman/CYEN301/
#
##########################################################################

#Steg
import sys

def parse(argv):
    #Defaults
    method = "b"
    direction = "s"
    offset = 0
    interval = 0
    wrapperfile = "wrapper.txt"
    hiddenfile = "hidden.txt"

    #invalid argument flag
    invalid = 0
    
    if (argv[0] == "-b"):
        method = "b"
    elif (argv[0] == "-B"):
        method = "B"
    else:
        invalid = 1
    if (argv[1] == "-s"):
        direction = "s"
    elif (argv[1] == "-r"):
        direction = "r"
    else:
        invalid = 1
    if (argv[2][0:2] == "-o"):
        if (argv[2][2:] != None):
            offset = argv[2][2:]
        else:
            invalid = 1
    indnum = 3
    if (argv[indnum][0:2] == "-i"):
        interval = argv[indnum][2:]
        indnum+=1
    else:
        invalid = 1
    if (argv[indnum][0:2] == "-w"):
        wrapperfile = argv[indnum][2:]
        indnum+=1
    else:
        invalid = 1
    if (len(argv)!= indnum):
        if (argv[indnum][0:2] == "-h"):
            hiddenfile = argv[indnum][2:]
        else:
            invalid = 1
    return method, direction, offset, interval, wrapperfile, hiddenfile, invalid      

#MAIN
variables = parse(sys.argv[1:])
if (variables[6] == 1):
    sys.stdout.write("Invalid argument")
else:
    method = variables[0]
    direction = variables[1]
    offset = variables[2]
    interval = variables[3]
    wrapperfile = variables[4]
    hiddenfile = variables[5]

    #debug print statements
    print ("method:",method)
    print ("direction:",direction)
    print ("offset:",offset)
    print ("interval:",interval)
    print ("wrapperfile:",wrapperfile)
    print ("hiddenfile:",hiddenfile)


