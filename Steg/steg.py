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

#deals with input at the command line and returns the relevent information as a tuple
def parse(argv):
    #Defaults
    method = "b"
    direction = "s"
    offset = 0
    interval = 0
    wrapperfile = "wrapper.txt"
    hiddenfile = "hidden.txt"
    outputfile = "none"
    redirection = False

    #invalid argument flag
    invalid = 0
    
    if (argv[0] == "-b"):                       # if the first argument is '-b' or '-B' set the method to bit or byte respectively, otherwise the input is invalid
        method = "b"
    elif (argv[0] == "-B"):
        method = "B"
    else:
        invalid = 1
    if (argv[1] == "-s"):                       # if the second argument is '-s' or '-r' set the direction to store or retrieve respectively, otherwise the input is invalid
        direction = "s"
    elif (argv[1] == "-r"):
        direction = "r"
    else:
        invalid = 1
    if (argv[2][0:2] == "-o"):                  # if the third argument starts with '-o' set the offset of the val, otherwise the input is invalid
        if (argv[2][2:] != None):
            offset = argv[2][2:]
        else:
            invalid = 1
    #indnum is the current index number for the arguments list
    indnum = 3
    #info for "-i<val>" parameter
    if (argv[indnum][0:2] == "-i"):             #if the current index starts with "-i"
        interval = argv[indnum][2:]             #       store the <val> into interval
        indnum+=1                               #       increment the index number
    if (argv[indnum][0:2] == "-w"):             #if the current index starts with "-w"
        wrapperfile = argv[indnum][2:]          #       store the <val> into wrapperfile
        indnum+=1                               #       increment the index number
    else:                                       # if the '-w' command does not exist, the input is invalid
        invalid = 1
    if (len(argv) > indnum):                    # if the current index number is still in bounds
        if (len(argv[indnum] > 1)):             #       if the length of the current index is greator than 1(in case this next value is ">" and not "-h")
            if (argv[indnum][0:2] == "-h"):     #           if the current index starts with "-h"
                hiddenfile = argv[indnum][2:]   #                   store the <val> into hiddenfile
                indnum+=1                       #                   increment the index number
    if (len(argv) > indnum):                    # if the current index number is still in bounds
        if (argv[indnum] == ">"):               #       if this index is '>'
            redirection = True                  #               set redirection flag to true
            indnum+=1
        else:                                   #if the next variable after '-h' is not '>' the input is invalid
            invalid = 1
    if (redirection):                           # if the previous redirection flag was set (to true)
        if (len(argv) > indnum)):               #       if the current index number is still in bounds
            outputfile = argv[indnum]           #               store this index into the output file
        else:
            redirection = False                 # if the current index number is not in bounds when redirection is set to true (meaning the user did not specify a file even though they entered '>'), set redirection to False
    return method, direction, offset, interval, wrapperfile, hiddenfile, redirection, outputfile, invalid      

#MAIN
variables = parse(sys.argv[1:])
if (variables[8] == 1):
    sys.stdout.write("Invalid argument")
else:
    method = variables[0]
    direction = variables[1]
    offset = variables[2]
    interval = variables[3]
    wrapperfile = variables[4]
    hiddenfile = variables[5]
    redirection = variables[6]
    outputfile = variables[7]

    #debug print statements
    print ("method:",method)
    print ("direction:",direction)
    print ("offset:",offset)
    print ("interval:",interval)
    print ("wrapperfile:",wrapperfile)
    print ("hiddenfile:",hiddenfile)
    print ("redirection:",redirection)
    print ("output file:",outputfile)


