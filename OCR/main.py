from flask import Flask, request, send_file

from preprocessing import preprocessing
from OCR import OCR
from text_correction import text_correction
from text_to_speech import text_to_speech

# to connect with flutter app **LOCALLY**
        # https://youtu.be/Su_qbc98xsE?feature=shared

app = Flask(__name__)
@app.route('/', methods=["GET"])
def hello():
    return 'this slash'
@app.route('/home', methods=["GET"])
def home():
    return 'this home'

@app.route('/pdf', methods=["POST"])
def ocr_pdf():
    # return send_file("mp3s/1.mp3", mimetype='audio/mp3')
    audio = text_to_speech(request.get_json()['text'])
    return send_file(audio, mimetype='audio/mp3')
# @app.route('/img', methods=["POST"])
# def ocr_img():
#     img = request.files['image']
#     preprocessed_img = preprocessing(img)
#     row_text = OCR(preprocessed_img)
#     final_text = text_correction(row_text)
#     audio = text_to_speech(final_text)
#     return send_file(audio, mimetype='audio/mp3')
 
if __name__ == '__main__':
    app.run(debug=True)
