import cv2
import numpy as np

labels = ['glioma', 'meningioma', 'notumor', 'pituitary']

def make_prediction(img_path, model):
    img = cv2.imread(img_path)

    img = cv2.resize(img, (224, 224))
    print(type(img), img.shape)

    img_As_Array = np.expand_dims(img, axis=0)
    print(type(img), img.shape)
 
    pred = model.predict(img_As_Array)
    print(f'Prediction: {pred}')

    predicted_class = np.argmax(pred[0])
    print(f'Class: {predicted_class}')

    predicted_label = labels[predicted_class]
    print(f'Label: {predicted_label}')

    return predicted_label