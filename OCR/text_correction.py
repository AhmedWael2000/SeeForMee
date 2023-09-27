from transformers import pipeline

def text_correction(text):
 fix_spelling = pipeline("text2text-generation",model="oliverguhr/spelling-correction-english-base")
 text = fix_spelling(text, max_length=30000)
 
    return text
