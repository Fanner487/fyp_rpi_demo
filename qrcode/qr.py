import os
#import qrtools
#import zbar
import picamera
#import qrtools
from time import sleep





camera = picamera.PiCamera()

strpath = "/home/pi/dev/qrcode/"

strfile = "qrtest"



countdown = 3



print "Taking a snapshot in"



while countdown > 1:



	print str(countdown)

	sleep(1)

	countdown -= 1





camera.capture("qrtest.png")

##print "Encoding url into qrcode"

# # call os command to create qr code with some data

##os.system("qrencode -o "+strpath+strfile+".png 'http://www.raspberrypi.org'")



print "Reading data from qrcode"

# call os command to read qr data to text file

os.system("zbarimg -q qrtest.png > qrtest.txt")



strreadtext = strpath+strfile+".txt"



if os.path.exists(strreadtext):

        strqrcode = open(strreadtext, 'r').read()

        print strqrcode

else:

        print "QR-Code text file not found"
