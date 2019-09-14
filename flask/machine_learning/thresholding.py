import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    ret2, thresh1 = cv2.threshold(fgmask, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('fgmask', frame)
    cv2.imshow('frame', thresh1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()