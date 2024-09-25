from flask import Flask, render_template, request, redirect, url_for
import os
from enhance import enhance_image
from recognition import recognize_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

   # Главная страница
@app.route('/')
def index():
    return render_template('index.html')

   # Обработка загруженного изображения
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)

           # Улучшение изображения
        enhanced_image_path = enhance_image(image_path)

           # Распознавание текста
        recognized_text = recognize_text(enhanced_image_path)

        return render_template('result.html', image_path=enhanced_image_path, text=recognized_text)



if __name__ == "__main__":
    app.run(debug=True)