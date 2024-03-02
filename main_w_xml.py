import cv2

FRAMEWIDTH = 480
FRAMEHEIGHT = 400

# Video feed
cap = cv2.VideoCapture(1)
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

def detectFire(frame):
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)
    for (x, y, w, h) in fire:
        cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (33,33,221), 2)

    cv2.waitKey(1)
    if len(fire):
        return 1
    return 0



def run():
    success, img = cap.read()
    img = cv2.resize(img, (FRAMEWIDTH, FRAMEHEIGHT))
    cv2.imshow('frame', img)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    Fire = detectFire(img)

    if Fire:
        return 1
    else:
        return 0


if __name__=="__main__":

    while True:
        res=run()
        if res ==1:
            print(res)