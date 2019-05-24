import sys
from pycipher import Caesar

### Main ###

# Check for arguments
if sys.argv < 2:
    raise Exception("CaesarCipher.py <1-25>")
try:
    # Make sure second argument is an int
    key = int(sys.argv[1])
except:
    print "Key must be an integer."
# Make sure key number is within 1-26
if key not in range(1,26):
    raise Exception("Key out of range.") 

# Get user input for encoded text
cypherText = raw_input()

# Split cypherText up by spaces
cypherText = cypherText.split(" ")

plainText = []

# Decode each word based on the key and add it to the plainText list
for word in cypherText:
    plainText.append(Caesar(key).decipher(word))

# Join everything together and print it
# Make everything lowercase because Caesar() prints it in upper
print " ".join(plainText).lower() 