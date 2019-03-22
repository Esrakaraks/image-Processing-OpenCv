import cv2
import numpy as np


result=cv2.VideoCapture(0)

while True:
    ret,square=result.read()
    area=square[100:200,100:200]
    cv2.imshow("video",square)
    cv2.imshow("video2",area)
    print(square)

    if cv2.waitKey(25) & 0xff == ord('q'):
        break
result.release()
cv2.destroyAllWindows()
