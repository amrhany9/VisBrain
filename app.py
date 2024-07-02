import os
from flask import Flask, jsonify, render_template, request, send_from_directory
from utils import file_handler, model_handler

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

model = model_handler.load_keras_model('./deep_learning/saved_models/basic_cnn_high_epochs')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(error='No file part')

    file = request.files['file']

    if file.filename == '':
        return jsonify(error='No selected file')

    result = file_handler.handle_file_upload(file, app.config['UPLOAD_FOLDER'], app.config['ALLOWED_EXTENSIONS'])

    if result is not None:
        filename, img_shape = result
        return jsonify(filename=filename, img_shape=img_shape)
    else:
        return jsonify(error='Invalid file format')

@app.route('/test', methods=['POST'])
def test_model():
    filename = request.form['filename']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    predicted_label = model_handler.handle_model_prediction(file_path, model)

    return jsonify(predicted_label=predicted_label)

# Serve uploaded files
@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
