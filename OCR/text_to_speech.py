from gtts import gTTS
import PyPDF2 as pdf
from io import BytesIO
import requests
from bs4 import BeautifulSoup

def text_to_speech(text):
    mp3_fo = BytesIO()
    speech = gTTS(text, lang='en')
    speech.save("mp3s/1.mp3")
    speech.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    return mp3_fo

def get_text_webpage(url):
    r = requests.get(url)  
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.get_text()
    return text