import cv2
import numpy as np
import base64
import skimage.io
from PIL import Image

def clean_image(image_variable):
    fgbg = cv2.createBackgroundSubtractorMOG2()


    # Capture frame-by-frame
    cleaned_image = decode(image_variable)


    frame = np.frombuffer(cleaned_image, dtype=np.float64)
    fgmask = fgbg.apply(frame)
    ret2, thresh1 = cv2.threshold(fgmask, 125, 255, cv2.THRESH_BINARY)


    thresh1 = thresh1.resize((128, 128))
    thresh1 = thresh1.reshape(1, 128, 128, 1)

    return thresh1

def decode(base64_string):
    if isinstance(base64_string, str):
        base64_string = base64_string.encode("latin1")

    print("b64 string", base64_string, type(base64_string))
    imgdata = base64.b64decode(base64_string)
    len(imgdata)
    print("IMG DATA", imgdata)
    image = Image.frombytes('RGB',(60,60),imgdata)

    # img = skimage.io.imread(imgdata, plugin='imageio')
    return img