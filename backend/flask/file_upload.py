from flask import Flask, request

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads/'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded.'
    file = request.files['file']
    if file.filename != '':
        file.save(app.config['UPLOAD_FOLDER'] + file.filename)
        return 'File uploaded successfully.'
    return 'No selected file.'

if __name__ == '__main__':
    app.run(debug=True)
