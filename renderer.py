import numpy as np
import cv2

cap = cv2.VideoCapture('test.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()