##########################################################
BinaryDecoder
##########################################################
This program can decode 7-bit or 8-bit binary encoded messages.

example usage:
you have a text file named binary1.txt

binary1.txt
100100011001011101100110110011011110100000101011111011111110010110110011001000100001

use in command line like so:

> python BinaryDecoder.py < binary1.txt

Hello World!

or if you want your result to go in another file

> python BinaryDecoder.py < binary1.txt > anotherfile.txt

the "Hello World!" output will be in anotherfile.txt in the same directory as the BinaryDecoder.py file

##########################################################
Chat Covert Channel
##########################################################
This program extracts a covert message from the delays in between characters of a message transmitted
by a chat server.

example usage(THIS ONLY WORKS ON LINUX):

> python ChatCovertChannelclient.py
Some sort of overt message is being transmitted here. But there is a
hidden message being covertly transmitted! Can you guess it?

Covert message: Gourd is 31337! Of course, we already knew this...

##########################################################
FTP Covert Channel
##########################################################
This program can extract a covert message from the file permissions of an ftp server using the 10 bit
or 7 bit methods.

You will see at the top of the py file METHOD = 10 and workdir = "10"
this means that at the moment the method we are using is the 10 bit method so the entire 
"-r--r---wx" is counted in the reading so append 0100100011 to the binary string
if it was the 7 bit method it would only read
"-r--r--"-wx so it would only append 0100100 to the binary string

this line connects to the ftp server the username and password may need to change
ftp = ftplib.FTP('jeangourd.com','anonymous','')

if there is a required port number, this code may help instead
ftp = ftplib.FTP()
ftp.connect('138.47.148.167', 8008)
ftp.login('spartans', 'spartansSPARTANSspartans')


example usage:
> python fetch.py
This is my C0V3rt message! Bwahahahahaha!


##########################################################
Steg
##########################################################
Steg
This program implements the steg algorithm that allows encoding and decoding messages in images

you should only use linux with this program since the results will be strange if doing it on windows.

syntax:
python steg.py -(bB) -(sr) -o<val> [-i<val>] -w<val> [-h<val>]
-b Use the bit method
-B Use the byte method
-s Store (and hide) data
-r Retrieve hidden data
-o<val> Set offset to <val>
-i<val> Set interval to <val>
-w<val> Set wrapper file to <val>
-h<val> Set hidden file to <val>

example usage, this stores the image secret.jpg into image.jpg and outputs the result in new.jpg
python steg.py -B -s -o1024 -i256 -wimage.jpg -hsecret.jpg > new.jpg

example usage 2, this retrieves a hidden image from new.jpg and outputs the result into extracted.jpg\
python steg.py -B -r -o1024 -i256 -wnew.jpg > extracted.jpg

##########################################################
Timelock
##########################################################
This program implements the timelock algorithm, it takes epoch time as input and current time is the current
system time

the algorithm goes like this
timeelapsed = currenttime - epochtime
messagedigest = MD5(MD5(timeelapsed))
code = (first two alphebetic characters in messagedigest) + (last two numeric characters in message digest in reverse order)
print code

example usage
epoch.txt
2017 01 01 00 00 00
current system time: 2017 03 23 18 02 06
> python timelock.py < epoch.txt
fa51

current system time: 2017 04 23 18 02 30
> echo "1999 12 31 23 59 59" | python timelock.py
ca45

current system time: 2010 06 13 12 55 34
> echo "2001 02 03 04 05 06" | python timelock.py
dd15


"timelockChallenge.py" has the ability to do an offset 
from the current time and connect to an ftp server immediately with the resulting code.
##########################################################
Timelock Challenge
##########################################################
change server and port and username at top of file

Offset times are if the current time on his server is different than the current time. Example if he says his server is ‘two hours behind’ change offsetHours to 2 and makes sure “subOffset=True”
if for example server is two hours ahead, subOffset=False

check if current time and epoch time are hardcoded and if they should/shouldnt be

if connecting to the server was successful you will see the ftp files automatically. I dont know if it will show hiddenfiles but if anything the “code” produced by timelock is printed out so we can login through terminal instead if needed

In the timelockChallenge.py after logging into the server
ls to list the files
cd <dirname> to change directory
get <filename> to download a file into the “challenge folder”
##########################################################
Vigenere Cipher
##########################################################
This program mathematically implements vigenere cipher

example usage:
> python vigenere -e mykey
hello <-- I typed this
tcvpm <-- my code generated this
HELLO <-- I typed this
TCVPM <-- my code generated this
^D <-- I pressed Ctrl+D (sometimes, this is needed twice)

>python vigenere -e "This is my key" > ciphertext.txt

Get ready for Cyber Storm! We’re going to turn your world upside down on May 24!
^D

in ciphertext.txt
Zlb jmspw psp Vfjwz Kfmbq! Ux’ym ywaze ds rnyv qwmd uyvjw bxkqvq byal hu Usg 24!
##########################################################
Xor
##########################################################
xor.py
the key file is named “key” by default
change “keyfile” variable in xor.py if the downloaded key file name is not just “key”

Works on linux only. Python 2. newfile may be an image with .jpg or sound .mp3
example usage:
python xor.py < yourdownloadedfile >  newfile
