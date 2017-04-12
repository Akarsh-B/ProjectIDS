"""
Takes pictures from the Raspberry Pi Camera at regular intervals. Detects faces
and sends cropped pictures of faces to the server
"""

import cv2
import requests


SERVER_URL = 'http://127.0.0.1:5000/image'
cascPath = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
executor = ThreadPoolExecutor(max_workers=2)


class FaceDetection(object):

    def __init__(self):
        pass

    def perform_detection(frame):
        img = cv2.imread(frame, 0)

        faces = cls.faceCascade.detectMultiScale(
            img,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Send each face to the server
        for (x, y, w, h) in faces:

            # OPTIMIZE: use Bytes.IO instead of storing the image on disk
            cv2.imwrite('cropped.jpg', img[y:y + h, x:x + w])

            # Send the image using the requests library
            files = {'file': open('cropped.jpg', 'rb')}

            requests.post(SERVER_URL, files=files)

            # TODO: delete `cropped.jpg`

    @classmethod
    def detect(cls, frame):
        executer.submit(perform_detection, frame)
