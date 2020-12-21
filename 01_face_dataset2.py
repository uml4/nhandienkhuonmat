import cv2
# from picamera.array import PiRGBArray
# from picamera import PiCamera
import numpy as np 
import os
import sys

# camera = PiCamera()
camera = cv2.VideoCapture(0)
camera.set(3, 640) # set video width
camera.set(4, 480) # set video height
# camera.resolution = (640, 480)
# camera.framerate = 30
# rawCapture = PiRGBArray(camera, size=(640, 480))

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

name = input("Nhap ten cua Anh/chi? ")
dirName = "./dataset/" + name
print(dirName)
if not os.path.exists(dirName):
	os.makedirs(dirName)
	print("Directory Created")
else:
	print("Name already exists")
	sys.exit()

count = 1
while(True):

	frame, img = camera.read()
	# img = cv2.flip(img, -1) # flip video image vertically
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)

	for (x, y, w, h) in faces:
		roiGray = img[y:y+h, x:x+w]


		
		# cv2.imshow("face", img)
		# cv2.imshow("face", roiGray)
		fileName = dirName + "/" + name + str(count) + ".jpg"
		cv2.imwrite(fileName, img)
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		count += 1

	cv2.imshow("face", img)	
		
		

	# cv2.imshow('frame', frame)
	k = cv2.waitKey(200) & 0xff # Press 'ESC' for exiting video
	if k == 27:
		break
	elif count >= 30: # Take 30 face sample and stop video
		break

cv2.destroyAllWindows()