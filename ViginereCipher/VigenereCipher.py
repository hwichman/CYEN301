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
    for x, y in zip(text, key):
        z = (alphabet.index(x) + alphabet.index(y)) % 26
        # Add the letter at the index to the final string
        cypher += alphabet[z]
    print(cypher)

def decode (key, cypher):
    plaintext = ""
    # Loop through both strings and run them through the decode equation
    for x, y in zip(cypher, key):
        z = (26 + alphabet.index(x) - alphabet.index(y)) % 26
        # Add the letter at the index to the final string
        plaintext += alphabet[z]
    print(plaintext)


def main(argv):
    userInput = ""

    # Set Arguments and error handling
    try:
        opts, args = getopt.getopt(argv, "e:d:")
    except getopt.GetoptError:
        print("VigenereCipher.py -e <key> or -d <key>")
        sys.exit(2)

    # Prompt user for input
    print("Please input text: ")
    userInput = input()

    # Check for arguments
    for opt, arg in opts:
        key = arg
        if opt == "-e":
            encode(key, userInput)
        elif opt == "-d":
            decode(key, userInput)
            
# Call main on program start
if __name__ == "__main__":
       main(sys.argv[1:])

