import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

### Main ###

# Check for arguments
if sys.argv < 2:
    raise Exception("CaesarCipher.py <1-25>")
try:
    # Make sure second argument is an int
    key = int(sys.argv[1])
except:
    print "Key must be an integer."

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
        x = alphabet.index(character)
        x = (x - key) % 26
        # Decrypted character is the character at the new index
        character = alphabet[x]
        # Add character to decrypted word
        plainWord.append(character)
    plainWord = "".join(plainWord)
    plainText.append(plainWord)

# Join everything together and print it
# Make everything lowercase because Caesar() prints it in upper
print " ".join(plainText).lower() 