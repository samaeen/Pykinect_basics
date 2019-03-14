from pykinect import nui
import numpy
import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def faceDetect(video):	
	gray=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3,minSize=(80, 80),flags=0)
	for (x,y,w,h) in faces:
		cv2.rectangle(video,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.imshow('KINECT Video Stream', video)

def video_handler_function(frame):
    video = numpy.empty((480,640,4),numpy.uint8)
    frame.image.copy_bits(video.ctypes.data)
    faceDetect(video)

kinect = nui.Runtime()
kinect.video_frame_ready += video_handler_function
kinect.video_stream.open(nui.ImageStreamType.Video, 2,nui.ImageResolution.Resolution640x480,nui.ImageType.Color)
cv2.namedWindow('KINECT Video Stream', cv2.WINDOW_AUTOSIZE)
print('ada')

while True:

    if cv2.waitKey(30)& 0xff==ord('q'):
    	break

kinect.close()
cv2.destroyAllWindows()