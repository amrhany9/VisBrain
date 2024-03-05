# file_handler.py

from flask import request, redirect
from werkzeug.utils import secure_filename
import os
import cv2

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def handle_file_upload(file, upload_folder, allowed_extensions):
    if file and allowed_file(file.filename, allowed_extensions):
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)

        # Load and preprocess the image to get its shape
        img = cv2.imread(file_path)
        img_shape = img.shape[0:]
        print(img_shape)

        return filename, img_shape
    else:
        return None, None