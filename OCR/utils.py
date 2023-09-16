import requests
from bs4 import BeautifulSoup
import PyPDF2
import spacy
import random


def get_text_webpage(url):
    r = requests.get(url)  
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.get_text()
    return text

def get_text_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in pdf_reader.pages:
                text += page.extract_text()
    return text



# url = "https://www.reuters.com/markets/global-markets-wrapup-1-2023-09-08/"
# print(get_text_webpage(url))

# pdf_path = "C:/Users/abdel/Downloads/Find My Place Festival Calendar Aug-Sept.pdf"
# print(get_text_pdf(pdf_path))