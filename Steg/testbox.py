method = "b"
direction = "r"
offset = 1024
interval = 1
wrapperfile = "steggedtest.bmp"
hiddenfile = "incaflag.bmp"
outputfile = "unsteggedtest.bmp"

sentinel = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]

# encrypts a file using steganography
def ensteg():
    global offset
    
    # reads hiddenfile into a byte array 'hiddenbytes'
    with open(hiddenfile, "rb") as hidden:
        hread = hidden.read()
        hiddenbytes = bytearray(hread)
        
    # reads wrapperfile into a byte array 'wrapperbytes'
    with open(wrapperfile, "rb") as wrapper:
        wread = wrapper.read()
        wrapperbytes = bytearray(wread)
        
    # Byte Method
    if (method == "B"):
        i = 0
        while (i < len(hiddenbytes)):
            wrapperbytes[offset] = hiddenbytes[i]
            offset += interval
            i += 1

        # insert sentinel
        i = 0
        while (i < len(sentinel)):
            wrapperbytes[offset] = sentinel[i]
            offset += interval
            i += 1
             
    # Bit Method
    if (method == "b"):
        # adds sentinel to hiddenbytes array
        for byte in sentinel:
            hiddenbytes.append(byte)
        i = offset
        j = 0
        while (j < len(hiddenbytes)):
            for k in range(8):
                wrapperbytes[i] &= 0b11111110
                wrapperbytes[i] |= ((hiddenbytes[j] & 0b10000000) >> 7)
                # zeroes most sig. bit before shift
                hiddenbytes[j] &= 0b01111111
                hiddenbytes[j] <<= 1
                i += interval
            j += 1

    # writes the new file
    sys.stdout(wrapperbytes)
    #steggedfile = open(outputfile, "wb+")
    #steggedfile.write(wrapperbytes)



# decrypts a file using steganography
def desteg():
    
    # reads wrapperfile into a byte array 'wrapperbytes'
    with open(wrapperfile, "rb") as wrapper:
        wread = wrapper.read()
        wrapperbytes = bytearray(wread)

    # creates empty byte array for hidden bytes
    hiddenbytes = bytearray([])
        
    # Byte Method
    if (method == "B"):
        i = offset
        # creates a test for sentinel
        sentineltest = []
        for j in range(len(sentinel)):
            sentineltest.append(wrapperbytes[i + j*interval])
        # checks the current byte plus next 5 bytes to see if it matches the sentinel (which will break the loop)
        while (sentineltest != sentinel):
            hiddenbytes.append(wrapperbytes[i])
            i += interval
            # updates the sentineltest list
            del sentineltest[0]
            sentineltest.append(wrapperbytes[i+interval*(len(sentinel)-1)])

    # Bit Method
    if (method == "b"):
        i = offset
        # creates a bit version of the sentinel
        # creates a byte for each bit in the original sentinel
        # where only the least significant bit is used
        bitsentinel = []
        for byte in sentinel:
            for k in range(8):
                temp = byte & 0b00000001
                bitsentinel.append(temp)
                byte >>= 1
        # creates a test for sentinel
        sentineltest = []
        for j in range(len(bitsentinel)):
            sentineltest.append(wrapperbytes[i + j*interval] & 0b00000001)
        while (sentineltest != bitsentinel):
            hiddenbyte = 0b00000000
            for k in range(8):
                hiddenbyte <<= 1
                hiddenbyte += wrapperbytes[i] & 0b00000001
                i += interval
                # updates the sentineltest list
                del sentineltest[0]
                sentineltest.append(wrapperbytes[i+interval*(len(bitsentinel)-1)] & 0b00000001)
            hiddenbytes.append(hiddenbyte)

    # writes the new file
    sys.stdout(hiddenbytes)
    #unsteggedfile = open(outputfile, "wb+")
    #unsteggedfile.write(hiddenbytes))



# encrypts or decrypts a file, based on specified direction
if direction == "s":
    ensteg()
else:
    desteg()
