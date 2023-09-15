from gtts import gTTS
import PyPDF2 as pdf
from io import BytesIO
def text_to_speech(book):
    
    # file = pdf.PdfReader(book)
    
    mp3_fo = BytesIO()
    text=book
    
    # for page in file.pages:
    #     text +=page.extract_text()
    
    speech = gTTS(text, lang='en')
    speech.write_to_fp(mp3_fo)
    speech.save('mp3s/1.mp3')

    # mp3_fo.seek(0)
    return mp3_fo