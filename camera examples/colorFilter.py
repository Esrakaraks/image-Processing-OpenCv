import cv2
import numpy as np


result=cv2.VideoCapture(0)
lowest=np.array([90,50,50])
highest=np.array([130,255,255])


while True:
    ret,view=result.read()
    hsv=cv2.cvtColor(view,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lowest,highest)
    colordetect=cv2.bitwise_and(view,view,mask=mask)
    #smoothed (yumuşatma)//gürültüleri engellemek için

    kernel=np.ones((15,15),dtype=np.float32)/225
    smoothed=cv2.filter2D(colordetect,-1,kernel)

    #Blur
    blur=cv2.GaussianBlur(colordetect,(15,15),0)
    cv2.imshow("blur",blur)
    #median
    median=cv2.medianBlur(colordetect,15)
    cv2.imshow("median",median)
    cv2.imshow("Mainview",view)
    cv2.imshow("smoothed",smoothed)
    cv2.imshow("hsv",hsv)
    cv2.imshow("result",colordetect)
    cv2.imshow("mask",mask)


    if cv2.waitKey(25) & 0xff ==ord('q'):
        break

result.release()
cv2.destroyAllWindows()

