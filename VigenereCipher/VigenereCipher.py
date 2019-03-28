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
#   Assignment 2 - Vingenere Cipher
#
#   Git Repo: https://github.com/hwichman/CYEN301/
#
##########################################################################

#Vingenere Cipher


# -e, -d command line args
# Grab key as command line arg then plaintext/cyphertext from stdin
# Run encode or decode according to command line arg
# print new text


import sys, getopt

# Alphabet for the cypher to use
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Encode text to cypher
def encode(key, text):
    cypher = ""
    # Loop through both strings and run them through the encode equation
    for x in range(0,len(text)):
        keyIndex = x % len(key)
        if (text[x].lower() not in alphabet):
            l = text[x]
        else:
            z = (alphabet.index(text[x].lower()) + alphabet.index(key[keyIndex].lower())) % 26
            if (text[x].isupper()):
                l = alphabet[z].upper()
            else:
                l = alphabet[z]
        # Add the letter at the index to the final string
        cypher += l
    print(cypher)

def decode (key, cypher):
    plaintext = ""
    # Loop through both strings and run them through the decode equation
    for x in range(0, len(cypher)):
        keyIndex = x % len(key)
        if (cypher[x].lower() not in alphabet):
            l = cypher[x]
        else:
            z = (26 + alphabet.index(cypher[x].lower()) - alphabet.index(key[keyIndex].lower())) % 26
            if (cypher[x].isupper()):
                l = alphabet[z].upper()
            else:
                l = alphabet[z]
        # Add the letter at the index to the final string
        plaintext += l
    print(plaintext)


def main(argv):
    userInput = ""

    # Set Arguments and error handling
    try:
        opts, args = getopt.getopt(argv, "e:d:")
    except getopt.GetoptError:
        print("VigenereCipher.py -e <key> or -d <key>")
        sys.exit(2)

    # Check for arguments
    for opt, arg in opts:
        key = arg
        while (1):
            userInput = input()
            if ("^D" in userInput):
                break
            elif opt == "-e":
                    encode(key, userInput)
            elif opt == "-d":
                decode(key, userInput)
            
# Call main on program start
if __name__ == "__main__":
       main(sys.argv[1:])

