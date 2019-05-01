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
    errormsg = ""
    if (len(argv) > 0):
        if (argv[0] == "-b"):                       # if the first argument is '-b' or '-B' set the method to bit or byte respectively, otherwise the input is invalid
            method = "b"
        elif (argv[0] == "-B"):
            method = "B"
        else:
            invalid = 1
            errormsg = "Syntax error: First argument is -b or -B"
            return invalid, errormsg
    else:
        invalid = 1
        errormsg = "Syntax Error: Not enough arguments"
        return invalid, errormsg
    if (len(argv) > 1):
        if (argv[1] == "-s"):                       # if the second argument is '-s' or '-r' set the direction to store or retrieve respectively, otherwise the input is invalid
            direction = "s"
        elif (argv[1] == "-r"):
            direction = "r"
        else:
            invalid = 1
            errormsg = "Syntax error: Second argument is -s or -r"
            return invalid, errormsg
    else:
        invalid = 1
        errormsg = "Syntax Error: Not enough arguments"
        return invalid, errormsg
    if (len(argv) > 2):
        if (argv[2][0:2] == "-o"):                  # if the third argument starts with '-o' set the offset of the val, otherwise the input is invalid
            if (argv[2][2:].isdigit()):
                offset = argv[2][2:]
            else:
                invalid = 1
                errormsg="Type Error: -o<val>, <val> must be an integer"
                return invalid, errormsg
        else:
            invalid = 1
            errormsg = "Syntax Error: Third argument is -o<val>"
            return invalid, errormsg
    else:
        invalid = 1
        errormsg = "Syntax Error: Not enough arguments"
        return invalid, errormsg
    #indnum is the current index number for the arguments list
    indnum = 3
    #info for "-i<val>" parameter
    if (len(argv) > indnum):
        if (argv[indnum][0:2] == "-i"):             #if the current index starts with "-i"
            if (argv[indnum][2:].isdigit()):        #       if <val> is valid
                interval = argv[indnum][2:]         #           store the <val> into interval
                indnum+=1                           #           increment the index number
            else:
                invalid = 1                         #       if <val> is not valid, the input in invalid
                errormsg="Type Error: -i<val>, <val> must be an integer"
                return invalid, errormsg
                print ("here")
    if (len(argv) > indnum):
        if (argv[indnum][0:2] == "-w"):             #if the current index starts with "-w"
            if (argv[indnum][2:] != ""):
                wrapperfile = argv[indnum][2:]      #       store the <val> into wrapperfile
                indnum+=1                           #       increment the index number
            else:
                invalid = 1
                errormsg = "TypeError: -w<val>, <val> cannot be empty"
                return invalid, errormsg
        else:                                       # if the '-w' command does not exist, the input is invalid
            invalid = 1
            errormsg = "Syntax error: -w command missing"
            return invalid, errormsg
    else:
        invalid = 1
        errormsg = "Syntax error: Not enough arguments"
        return invalid, errormsg
    if (len(argv) > indnum):                    # if the current index number is still in bounds
        if (argv[indnum][2:] != ""):
            if (argv[indnum][0:2] == "-h"):     #           if the current index starts with "-h"
                hiddenfile = argv[indnum][2:]   #                   store the <val> into hiddenfile
                indnum+=1                       #                   increment the index number
        else:
            invalid = 1
            errormsg = "TypeError: -h<val>, <val> cannot be empty"
            return invalid, errormsg
    return method, direction, offset, interval, wrapperfile, hiddenfile, invalid, errormsg      

#MAIN
variables = parse(sys.argv[1:])
if (variables[0] == 1):
    sys.stdout.write("Invalid argument\n")
    sys.stdout.write(variables[1]+"\n")
    sys.stdout.write("-(bB) -(sr) -o<val> [-i<val>] -w<val> [-h<val>]")
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


