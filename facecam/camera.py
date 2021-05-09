import cv2,os,urllib.request
import numpy as np
import time
from datetime import datetime
from django.conf import settings
face_detection_videocam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))
font = cv2.FONT_HERSHEY_SIMPLEX

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
		self.notdetectedstart = 0
		self.notdetected = 0

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)		
		for (x, y, w, h) in faces_detected:
			cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
			cv2.putText(image, str(current_time), (x, y), font, 0.7, (0, 0, 0), 2)
		ret, jpeg = cv2.imencode('.jpg', image)
		return jpeg.tobytes()

	def get_undetected_time(self):
    		return self.notdetected
