import pytesseract
from PIL import Image
import cv2
import os
from picamera import PiCamera
from time import sleep
camera = PiCamera()
#camera = ["http://192.168.1.56:4747/capture"]
camera.start_preview()
sleep(1)
while True:
	camera.capture('/home/pi/Desktop/mukul.jpg')
	camera.stop_preview()
	img = cv2.imread('/home/pi/Desktop/mukul.jpg') #Open the image from which charectors has to be recognized
	img = cv2.resize(img, (620,480) ) #resize the image if required
	cv2.imshow('img', img)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey to reduce detials
	gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise

	original = pytesseract.image_to_string(gray)
#test = (pytesseract.image_to_data(gray, lang=None, config='', nice=0) ) #get confidence level if required
#print(pytesseract.image_to_boxes(gray))
#print (original)


	if os.path.exists("/home/pi/Desktop/mukul.jpg"):
	  	os.remove("/home/pi/Desktop/mukul.jpg")
	else:
		print("The file does not exist")

	print (original)
#print (test)

