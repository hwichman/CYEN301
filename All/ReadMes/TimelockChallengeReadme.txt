change server and port and username at top of file

Offset times are if the current time on his server is different than the current time. Example if he says his server is ‘two hours behind’ change offsetHours to 2 and makes sure “subOffset=True”
if for example server is two hours ahead, subOffset=False

check if current time and epoch time are hardcoded and if they should/shouldnt be

if connecting to the server was successful you will see the ftp files automatically. I dont know if it will show hiddenfiles but if anything the “code” produced by timelock is printed out so we can login through terminal instead if needed

In the timelockChallenge.py after logging into the server
ls to list the files
cd <dirname> to change directory
get <filename> to download a file into the “challenge folder”