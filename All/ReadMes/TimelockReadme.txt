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