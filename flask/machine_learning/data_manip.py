import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime
import keyboard
from PIL import Image

IMG_FLDR = './data/gesture-7/'

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

record = False
imgs = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    ret2, thresh1 = cv2.threshold(fgmask, 125, 255, cv2.THRESH_BINARY)
    thresh1 = thresh1.T

    thresh = cv2.resize(thresh1, (438, 780))
    cv2.imshow('fgmask', thresh)


    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('s'):  # if key 'q' is pressed
            if not record:
                print('\nStart Recording!')
            else:
                print('\nStop Recording!')
            record = not record
        else:
            pass
    except:
        pass  # if user pressed a key other than the given key the loop will break

    if record:
        imgs += 1
        if imgs % 100 == 0:
            print(f'Recording, number of images: {imgs}')
        cv2.imwrite(IMG_FLDR + str(datetime.datetime.now()) + '.jpg', thresh1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()