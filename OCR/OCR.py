import pytesseract
from pytesseract import Output


myconfig = r"--psm 11 --oem 3"

def OCR(img):
    data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
    amount_box = len(data['text'])
    text = ""
    for i in range(amount_box):
        if float(data['conf'][i]) > 80:
            text += data['text'][i] + " "
    return text

