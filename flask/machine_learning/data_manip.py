import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
import keyboard

IMG_FLDR = 'data/test/'

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

record = False

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    ret2, thresh1 = cv2.threshold(fgmask, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('fgmask', frame)
    cv2.imshow('frame', thresh1)


    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('s'):  # if key 'q' is pressed
            record = not record
        else:
            pass
    except:
        pass  # if user pressed a key other than the given key the loop will break

    if record:
        print('Recording')
        cv2.imwrite(IMG_FLDR + str(datetime.datetime.now()) + '.jpg', thresh1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()