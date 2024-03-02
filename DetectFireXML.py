# Detecting Fire Using a xml file
import cv2

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')


def detectFire(frame):
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)
    for (x, y, w, h) in fire:
        cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (33,33,221), 2)
    cv2.imshow('frame', frame)
    if len(fire):
        return 1
    return 0


if __name__ == "__main__":
    FRAMEWIDTH = 480
    FRAMEHEIGHT = 400

    cap = cv2.VideoCapture(1)

    while True:
        success, img = cap.read()
        if not success:
            print("Error in Camera")
            break

        img = cv2.resize(img, (FRAMEWIDTH, FRAMEHEIGHT))
        Fire = detectFire(img)

        if Fire:
            print("There is FIRE !!")

        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
