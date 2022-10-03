import os
import pytesseract
from PIL import Image
from PyPDF2 import PdfFileMerger
from fpdf import FPDF

name = input('Enter your name: ')

# def filecreate(text):
#     file = '%s.txt' % (name)
#     with open(file, '+a') as f:
#         f.writelines(f'{text}')
#         f.close()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path = 'D:\\project\\Prescription\\Images'
mkdir = os.listdir(path)


# def imagescan():
#     for filename in mkdir:
#         filelocation = (path, filename)
#         myfile = '\\'.join(filelocation)
#         img = Image.open(myfile)
#         text = pytesseract.image_to_string(img)
#         filecreate(text)
#
def filecreate(name):
    file = '%s.txt' % (name)
    for filename in mkdir:
        filelocation = (path, filename)
        myfile = '\\'.join(filelocation)
        img = Image.open(myfile)
        text = pytesseract.image_to_string(img)
        with open(file, '+a') as f:
            f.writelines(f'{text}')
            f.close()


filecreate(name)