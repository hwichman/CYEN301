from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIOFLUSH
from sys import stdin, stdout

def on_press(key, interval):
    #print "{} pressed.".format(key)
    sleep(interval)

def on_release(key):
    print "{} released".format(key)

keyboard = Controller()
password = raw_input()
timings = raw_input()
print "password = {}".format(password)
print "timings = {}".format(timings)

password = password.split(",")
password = password[:len(password)/ 2 + 1]
password = "".join(password)

print password

string = password

timings = timings.split(",")
timings = [float(a) for a in timings]
keypress = timings[:len(timings)/2 + 1]
keyinterval = timings[len(timings)/2 + 1:]

print "key press times = {}".format(keypress)
print "key intervals = {}".format(keyinterval)

#tcflush(stdin, TCIOFLUSH)
i = 0
for char in string:

    keyboard.press(char)
    on_press(char, keypress[i])
    on_release(char)
    if i == len(string) - 1:
        break
    sleep(keyinterval[i])
    i += 1

stdout.flush()

