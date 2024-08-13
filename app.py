from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

# 업로드 폴더 경로 설정
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# PDF 파일 업로드 및 저장 API
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'pdf' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['pdf']
        
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        if file and file.filename.endswith('.pdf'):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({"message": "File uploaded successfully", "filename": filename}), 200
    
    return render_template('upload.html')

# 텍스트 입력 받는 페이지
@app.route('/text', methods=['GET', 'POST'])
def text_input():
    if request.method == 'POST':
        text = request.form['text']
        return jsonify({"message": "Text received", "text": text}), 200

    return render_template('text_input.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)