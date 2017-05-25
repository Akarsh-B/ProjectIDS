import cv2
import numpy as np 

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
cam.set(3,320)
cam.set(4,240)

rec=cv2.face.createLBPHFaceRecognizer()
rec.load('recognizer/trainingData.yml')
uid = 0
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
while True:
	ret,img=cam.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
		id,conf=rec.predict(gray[y:y+h,x:x+w])
		'''  
		if(uid == #uid of the person as in the image trained ):
			"write a statement at sends to the server the uid of the person,if there exists as uid of the person,on the server print his details and finally face recognized."
		elif (id == 2):
			"write a statement at sends to the server the uid of the person,if there exists as uid of the person,on the server print his details and finally face recognized."
        We can also add more elis if conditions
        '''
		cv2.putText(img,str(uid),(x,y+h), font, 1, (200,255,155), 2, cv2.LINE_AA)
	cv2.imshow("Face",img)
	if(cv2.waitKey(1) == ord('q')):
		break;
cam.release()
cv2.destroyAllWindows()

