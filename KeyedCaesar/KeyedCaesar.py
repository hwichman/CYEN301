import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

### Main ###

# Check for arguments
if sys.argv < 3:
    raise Exception("CaesarCipher.py <1-25> <alphabetKey>")

try:
    # Make sure second argument is an int
    numKey = int(sys.argv[1])
except:
    print "Key must be an integer."

alphaKey = sys.arv[2]

# New alphabet the cipher will use
# Starts with the alphaKey 
# Each character in the alphabet not in the alphaKey is added to the end of the alphaKey
for character in alphabet:
    if character not in alphaKey:
        alphaKey += character

# Get user input for encoded text
cypherText = raw_input()

# Split cypherText up by spaces
cypherText = cypherText.split(" ")

plainText = []


# Decode each word based on the key and add it to the plainText list
for word in cypherText:
    plainWord = ""
    for character in word:
        # Shift index of character by key.
        x = alphaKey.index(character)
        x = (x - numKey) % 26
        # Decrypted character is the character at the new index
        character = alphaKey[x]
        # Add character to decrypted word
        plainWord.append(character)
    plainWord = "".join(plainWord)
    plainText.append(plainWord)

# Join everything together and print it
# Make everything lowercase because Caesar() prints it in upper
print " ".join(plainText).lower()