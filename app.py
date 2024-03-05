import os
from flask import Flask, redirect, render_template, request, send_from_directory
from utils import file_handler, model_handler

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

model = model_handler.load_keras_model('./deep_learning/saved_models/Classification_Model')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('index.html')

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    result = file_handler.handle_file_upload(file, app.config['UPLOAD_FOLDER'], app.config['ALLOWED_EXTENSIONS'])

    if result is not None:
        filename, img_shape = result
        return render_template('index.html', filename=filename, img_shape=img_shape)
    else:
        return render_template('index.html', error='Invalid file format')

@app.route('/test', methods=['POST'])
def test_model():
    filename = request.form['filename']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    predicted_label = model_handler.handle_model_prediction(file_path, model)

    return render_template('index.html', filename=filename, predicted_label=predicted_label)

# Serve uploaded files
@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
