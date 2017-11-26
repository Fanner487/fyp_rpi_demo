import os
import picamera
from time import sleep

output_image_path = "scan.png"
output_qr_path = "result.txt"
camera = picamera.PiCamera()
countdown = 3

print "Taking a snapshot in"

# counts down from 3 before taking snapshot
while countdown > 0:

	print str(countdown)

	sleep(1)

	countdown -= 1


camera.capture(output_image_path)


print "Reading data from qrcode"


# call os command to read qr data to text file

os.system("zbarimg -q " + output_image_path + " > " + output_qr_path)



if os.path.exists(output_qr_path):

        strqrcode = open(output_qr_path, 'r').read()

        print strqrcode

else:

        print "QR-Code text file not found"
