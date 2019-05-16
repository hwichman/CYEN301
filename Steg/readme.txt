Steg
This program implements the steg algorithm that allows encoding and decoding messages in images

you should only use linux with this program since the results will be strange if doing it on windows.

syntax:
python steg.py -(bB) -(sr) -o<val> [-i<val>] -w<val> [-h<val>]
-b Use the bit method
-B Use the byte method
-s Store (and hide) data
-r Retrieve hidden data
-o<val> Set offset to <val>
-i<val> Set interval to <val>
-w<val> Set wrapper file to <val>
-h<val> Set hidden file to <val>

example usage, this stores the image secret.jpg into image.jpg and outputs the result in new.jpg
python steg.py -B -s -o1024 -i256 -wimage.jpg -hsecret.jpg > new.jpg

example usage 2, this retrieves a hidden image from new.jpg and outputs the result into extracted.jpg\
python steg.py -B -r -o1024 -i256 -wnew.jpg > extracted.jpg