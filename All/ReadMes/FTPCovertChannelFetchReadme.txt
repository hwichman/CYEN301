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

