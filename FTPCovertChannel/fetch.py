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

from ftplib import FTP

ftp = ftplib.FTP('jeangourd.com','anonymous','')

print "File List: "

files = ftp.dir()

print files





