import cv2
import numpy as np
import base64


fgbg = cv2.createBackgroundSubtractorMOG2()


# Capture frame-by-frame
s = base64.b64encode(insert_var_here)
r = base64.decodebytes(s)
frame = np.frombuffer(r, dtype=np.float64)
fgmask = fgbg.apply(frame)
ret2, thresh1 = cv2.threshold(fgmask, 125, 255, cv2.THRESH_BINARY)


thresh1 = thresh1.resize((128, 128))
thresh1 = thresh1.reshape(1, 128, 128, 1)