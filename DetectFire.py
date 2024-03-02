# This program is for detecting fire and This will return number of pixels from the image.
# This code is from Scratch

import cv2
import numpy as np

hsvVals = [9, 40, 229, 53, 229, 255]  # first 3 ar minimum values and second 3 are maximum values
FIREPXL =100

def detectFire(img):
    imgBlur = cv2.GaussianBlur(img, (15, 15), 0)
    imgHsv = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2HSV)
    lower = np.array(hsvVals[:3])
    higher = np.array(hsvVals[3:])
    mask = cv2.inRange(imgHsv, lower, higher)
    # result = cv2.bitwise_and(img, img, mask=mask)

    # Count Fire pixel before converting mask gray to bgr
    pxl = cv2.countNonZero(mask)
    # print(pxl)

    # mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    # Display pixel Counting
    cv2.rectangle(img, (200, 10), (300, 40), (0, 255, 0), thickness=2)
    cv2.putText(img, str(pxl), (225, 33), fontFace=cv2.FONT_HERSHEY_COMPLEX,
                fontScale=0.8, thickness=2, color=(0, 0, 255))
    cv2.imshow('Camera', img)
    if pxl>FIREPXL:
        return 1
    return 0


if __name__ == "__main__":
    FRAMEWIDTH = 480
    FRAMEHEIGHT = 400

    cap = cv2.VideoCapture(1)

    while True:
        success , img = cap.read()
        if not success:
            print("Error in Camera")
            break

        img = cv2.resize(img, (FRAMEWIDTH, FRAMEHEIGHT))
        Fire = detectFire(img)

        if Fire:
            print("There is FIRE !!")
        else:
            print("No fire.")

        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
