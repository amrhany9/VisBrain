import cv2
import numpy as np

labels = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

descriptions = {
    "Glioma": "Gliomas are tumors that arise from glial cells in the brain or spine.",
    "Meningioma": "Meningiomas are tumors that arise from the meninges, the membrane that surrounds the brain and spinal cord.",
    "Pituitary": "Pituitary tumors are abnormal growths that develop in the pituitary gland.",
    "No Tumor": "No tumor detected in the provided image."
}

def make_prediction(img_path, model):
    img = cv2.imread(img_path)

    img = cv2.resize(img, (224, 224))
    print(type(img), img.shape)

    img = img / 255.0

    img_As_Array = np.expand_dims(img, axis=0)
    print(type(img), img.shape)
 
    pred = model.predict(img_As_Array)
    print(f'Prediction: {pred}')

    predicted_class = np.argmax(pred[0])
    print(f'Class: {predicted_class}')

    predicted_label = labels[predicted_class]
    print(f'Label: {predicted_label}')

    description = descriptions[predicted_label]
    print(f'Description: {description}')

    return predicted_label, description