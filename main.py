from pytesseract import pytesseract
import os
class OCR:
    def __init__(self):
        self.path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def extract(self, filename):
        pytesseract.tesseract_cmd = self.path

        text = pytesseract.image_to_string(filename)
        return text

ocr = OCR()
text1 = ocr.extract('images/img1.jpg')
print('here is test1', text1)

#this one does not work
text2 = ocr.extract('images/img2.jpg')
print('here is test2', text2)

text3 = ocr.extract('images/russiatext.png')
print('here is test3', text3)