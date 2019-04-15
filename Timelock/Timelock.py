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
import hashlib
currentTime = "2013 05 06 07 43 25"
#currentTime = datetime.now(tzinfo=None)
epochTime= "1999 12 31 23 59 59"

class dst():
	def __init__(self, startMonth, startDay, endMonth, endDay):
		self.startMonth = startMonth
		self.startDay = startDay
		self.endMonth = endMonth
		self.endDay = endDay

dstDict = {1966:dst(4,24,10,30), 1999:dst(4,4,10,31), 2013:dst(3,10,11,3)}
	
def DSTApplies(dateTime1, dateTime2):
	if (isInDST(dateTime1) and isInDST(dateTime2)):
		return False
	elif (not isInDST(dateTime1) and not isInDST(dateTime2)):
		return False
	else:
		return True
	
def isInDST(dateTimeObj):
	year = dateTimeObj.year
	dstYear = dstDict[year]
	startDate = datetime.datetime(year, dstYear.startMonth, dstYear.startDay, 2, 0, 0)
	endDate = datetime.datetime(year, dstYear.endMonth, dstYear.endDay, 2, 0, 0)
	if (dateTimeObj > startDate and dateTimeObj < endDate):
		return True
	else:
		return False

def timeStringToDatetime(timeString):
	return datetime.datetime(int(timeString[:4]),int(timeString[5:7]),int(timeString[8:10]), int(timeString[11:13]), int(timeString[14:16]), int(timeString[17:19]))

def digestedTimeDifferenceToCode(digestedTime):
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

def addtzOffset(dateTimeObj, offsetHrs):
	dateTimeObj.hour = dateTimeObj.hour + offsetHrs

#Main
epochTime = timeStringToDatetime(epochTime)
currentTime = timeStringToDatetime(currentTime)


#calculate the time difference
timeDifference = currentTime - epochTime

print ("time difference: ",timeDifference)

#convert the timedelta to an integer time difference in seconds and apply daylight savings if needed
timeDifferenceInSeconds = 86400*timeDifference.days + timeDifference.seconds
if (DSTApplies(epochTime, currentTime)):
	timeDifferenceInSeconds -= 3600
print ("time difference in seconds: ",timeDifferenceInSeconds)

#rounds the time down to the nearest divisibility by 60
usableTimeDifference = timeDifferenceInSeconds - timeDifferenceInSeconds%60
print ("usable time difference: ",usableTimeDifference)

#digest this usableTime difference twice
digestedTime = hashlib.md5(hashlib.md5(str(usableTimeDifference)).hexdigest()).hexdigest()
print ("digestedTime: ",digestedTime)

#takes the first two alphabetic characters from the right and the first two numeric from the left to get the code
code = digestedTimeDifferenceToCode(digestedTime)

print (code)

