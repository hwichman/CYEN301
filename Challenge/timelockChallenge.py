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
#   Assignment 5 - Timelock
#   Git Repo: https://github.com/hwichman/CYEN301/
#
##########################################################################

#Timelock
import datetime
import md5
import sys
import ftplib
import os
import time
allowHardcodedCurrentTime = True
allowHardcodedEpochTime = True
hardcodedCurrentTime = "2017 04 26 15 14 30"
hardcodedEpochTime= "1974 06 01 08 57 23"
#set true the offset is being subtracted from the current time, set false if the offset is being added instead
subOffset = False
offsetDays = 0
offsetHours = 0
offsetMinutes = 0
offsetSeconds = 0
interval=0.05

ftpIP= "speedtest.tele2.net"
ftpPort = None
ftpUser = "anonymous"

#ftpIP= "jeangourd.com"
#ftpPort = 8008
#ftpUser = "spartans"


####Daylight savings stuff####
#a class containing the start month/day and end month/day of daylight savings
class dst():
	def __init__(self, startMonth, startDay, endMonth, endDay):
		self.startMonth = startMonth
		self.startDay = startDay
		self.endMonth = endMonth
		self.endDay = endDay

#A historical list of daylight savings date and times
dstDict = {1966:dst(4,24,10,30),1967:dst(4,30,10,29),1968:dst(4,28,10,27),1969:dst(4,27,10,26),1970:dst(4,26,10,25), \
           1971:dst(4,25,10,31),1972:dst(4,30,10,29),1973:dst(4,29,10,28),1974:dst(1, 6,10,27),1975:dst(2,23,10,26), \
           1976:dst(4,25,10,31),1977:dst(4,24,10,30),1978:dst(4,30,10,29),1979:dst(4,29,10,28),1980:dst(4,27,10,26), \
           1981:dst(4,26,10,25),1982:dst(4,25,10,31),1983:dst(4,24,10,30),1984:dst(4,29,10,28),1985:dst(4,28,10,27), \
           1986:dst(4,27,10,26),1987:dst(4, 5,10,25),1988:dst(4, 3,10,30),1989:dst(4, 2,10,29),1990:dst(4, 1,10,28), \
           1991:dst(4, 7,10,27),1992:dst(4, 5,10,25),1993:dst(4, 4,10,31),1994:dst(4, 3,10,30),1995:dst(4, 2,10,29), \
           1996:dst(4, 7,10,27),1997:dst(4, 6,10,26),1998:dst(4, 5,10,25),1999:dst(4, 4,10,31),2000:dst(4, 2,10,29), \
           2001:dst(4, 1,10,28),2002:dst(4, 7,10,27),2003:dst(4, 6,10,26),2004:dst(4, 4,10,31),2005:dst(4, 3,10,30), \
           2006:dst(4, 2,10,29),2007:dst(3,11,11, 4),2008:dst(3, 9,11, 2),2009:dst(3, 8,11, 1),2010:dst(3,14,11, 7), \
           2011:dst(3,13,11, 6),2012:dst(3,11,11, 4),2013:dst(3,10,11, 3),2014:dst(3, 9,11, 2),2015:dst(3, 8,11, 1), \
           2016:dst(3,13,11, 6),2017:dst(3,12,11, 5),2018:dst(3,11,11, 4),2019:dst(3,10,11, 3),2020:dst(3, 8,11, 1)}

def grabFile(filename):

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename+"/Destination", localfile.write, 1024)

    ftp.quit()
    localfile.close()

#returns true if one datetime is in daylight savings while the other is not	
def DSTApplies(dateTime1, dateTime2):
	if (isInDST(dateTime1) and isInDST(dateTime2)):
		return False
	elif (not isInDST(dateTime1) and not isInDST(dateTime2)):
		return False
	else:
		return True

#returns true if the datetime object is in daylight savings time	
def isInDST(dateTimeObj):
	year = dateTimeObj.year
	dstYear = dstDict[year]
	startDate = datetime.datetime(year, dstYear.startMonth, dstYear.startDay, 2, 0, 0)
	endDate = datetime.datetime(year, dstYear.endMonth, dstYear.endDay, 2, 0, 0)
	if (dateTimeObj > startDate and dateTimeObj < endDate):
		return True
	else:
		return False

####Conversion stuff####
def timeStringToDatetime(timeString):
	return datetime.datetime(int(timeString[:4]),int(timeString[5:7]),int(timeString[8:10]), int(timeString[11:13]), int(timeString[14:16]), int(timeString[17:19]))

#takes the MD5 digest as a parameter and returns a code that is 4 characters long: the first two characters are the first two alphabetic characters
#starting from the left of the digest and the first two numeric characters starting from the left of the digest
def digestedTimeDifferenceToCode(digestedTime):
        #string variables to append characters to
	codeLetters = ""
	codeNumbers = ""
	for i in range(0,len(digestedTime)):
		if (len(codeLetters) == 2 and len(codeNumbers) == 2):
			break
		if (len(codeLetters) is not 2):
			if (digestedTime[i].isalpha()):
				codeLetters += digestedTime[i]
		if (len(codeNumbers) is not 2):
			if (not digestedTime[len(digestedTime)-1-i].isalpha()):
				codeNumbers += digestedTime[len(digestedTime)-1-i]
	code = codeLetters+codeNumbers
	return code


def grabfile(filename, path=""):
	localfile = open(filename, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	localfile.close()

######   MAIN    #######
if (allowHardcodedCurrentTime):
	print ("Warning: Hard-coded time variables is enabled.")
	print ("Current Time: "+hardcodedCurrentTime)
	dtCurrentTime = timeStringToDatetime(hardcodedCurrentTime)
else:
	dtCurrentTime = datetime.datetime.now()

if (allowHardcodedEpochTime):
        print ("Warning: Hard-coded time variables is enabled.")
	print ("Epoch Time  : "+hardcodedEpochTime)
	dtEpochTime = timeStringToDatetime(hardcodedEpochTime)
else:
        line = sys.stdin.readline()
	dtEpochTime = timeStringToDatetime(line)


#add offset
if (subOffset):
        oCurrentTime = dtCurrentTime - datetime.timedelta(days=offsetDays,hours=offsetHours,minutes=offsetMinutes,seconds=offsetSeconds)
else:
        oCurrentTime = dtCurrentTime - datetime.timedelta(days=offsetDays,hours=offsetHours,minutes=offsetMinutes,seconds=offsetSeconds)

#calculate the time difference
timeDifference = oCurrentTime - dtEpochTime

#convert the timedelta to an integer time difference in seconds
timeDifferenceInSeconds = 86400*timeDifference.days + timeDifference.seconds

#applies daylight savings (if one time xor the other time is in dst)
if (DSTApplies(dtEpochTime, dtCurrentTime)):
	timeDifferenceInSeconds -= 3600

#rounds the time down to the nearest divisibility by 60
usableTimeDifference = timeDifferenceInSeconds - timeDifferenceInSeconds%60

#digest this usableTime difference twice
digestedTime = md5.md5(md5.md5(str(usableTimeDifference)).hexdigest()).hexdigest()

#takes the first two alphabetic characters starting from the left and the first two numeric starting from the right to get the code
code = digestedTimeDifferenceToCode(digestedTime)

print (code)
#connects to ftp server


ftp = ftplib.FTP()

#ftp.connect(ftpIP)
ftp.connect(ftpIP, ftpPort)
ftp.login(ftpUser, code)

#empty list to contain strings of file information
files = []

#adds file information of each file to array
ftp.dir(files.append)

for line in files:
	print line

usrIn = sys.stdin.readline()
data = usrIn.split()
while (data[0] != "close"):
	if ("cd" in data[0]):
		ftp.cwd(data[1])
	if ("ls" in data[0]):
		#empty list to contain strings of file information
		files = []
		#adds file information of each file to array
		ftp.dir(files.append)
		for line in files:
			print line
	if ("get" in data[0]):
		grabfile(data[1])
	usrIn = sys.stdin.readline()	
	data = usrIn.split()
	

grabfile("1KB.zip")
ftp.close()







