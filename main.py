import cv2
import numpy as np
import keras

# Video feed
cap = cv2.VideoCapture(2)
model = keras.models.load_model('fire_model.h5')


def run():
    success, image= cap.read()
    cv2.imshow("Camera",image)
    image = cv2.resize(image, (224, 224))
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # image= image/255.0
    image = np.expand_dims(image, axis=0)
    predict = model.predict(image)
    pred=np.where(predict >= 0.5, 1, 0)

    cv2.waitKey(1)
    return pred

if __name__=="__main__":
    while True:
        res=run()
        if res ==1:
            print(res)