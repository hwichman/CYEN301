method = "b"
direction = "s"
offset = 1024
interval = 1
wrapperfile = "incaflag2.bmp"
hiddenfile = "incaflag.bmp"
outputfile = "steggedtest.bmp"

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
                wrapperbytes[i] &= 0b1111110
                wrapperbytes[i] |= ((hiddenbytes[j] & 0b10000000) >> 7)
                # zeroes most sig. bit before shift
                hiddenbytes[j] &= 0b01111111
                hiddenbytes[j] <<= 1
                i += interval
            j += 1

    # writes the new file
    steggedfile = open(outputfile, "wb+")
    steggedfile.write(wrapperbytes)



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
        while ((i+6 < len(wrapperbytes)) and (sentineltest != sentinel)):
            hiddenbytes.append(wrapperbytes[i])
            i += interval
            # updates the sentineltest list
            del sentineltest[0]
            sentineltest.append(wrapperbytes[i+interval*5])

    # Bit Method
    #if (method == "b"):

    # writes the new file
    unsteggedfile = open(outputfile, "wb+")
    unsteggedfile.write(hiddenbytes)



# encrypts or decrypts a file, based on specified direction
if direction == "s":
    ensteg()
else:
    desteg()
