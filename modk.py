from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("modelkeras/keras_model.h5", compile=False)

# Load the labels
class_names = open("modelkeras/labels.txt", "r").readlines()

# Video feed
cap = cv2.VideoCapture(2)


def run():
    success, image= cap.read()
    cv2.imshow("Camera",image)

    # Resize the image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Make the image a numpy array and reshape it to the model's input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predict the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Wait for any key press to close the window
    cv2.waitKey(1)


if __name__=="__main__":
    while True:
        run()

cv2.destroyAllWindows()