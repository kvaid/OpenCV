import cv2
import numpy as np
import time

face_cascade = cv2.CascadeClassifier('..\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('..\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        # Draw rectangle where face is found at coordinates (top left), (bottom right)
        # cv2.rectangle(img,(200,200),(300,300),(0,255,0),3)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  
        # Limit Region-Of-Image (roi) for eye detection to the area where the face was found (between x,x+w and y,y+h)
        roi_gray = gray[y:y+h, x:x+w]                 
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
