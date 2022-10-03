import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def filecreate(name):
    path = 'D:\\project\\Prescription\\Images'
    mkdir = os.listdir(path)
    file = '%s.txt' % (name)
    for filename in mkdir:
        filelocation = (path, filename)
        myfile = '\\'.join(filelocation)
        img = Image.open(myfile)
        text = pytesseract.image_to_string(img)
        with open(file, '+a') as f:
            f.writelines(f'{text}')
            f.close()
    return file


string1 = ['T3', 'T4', 'TSH']
# fileis = "D:\\project\\Prescription\\Testing.txt"
file1 = open(filecreate('Testing'), "+r")
savePath = 'D:\\project\\Prescription\\NewFiles\\'
filename = '%s_%s_%s_Pathology.txt' % ('Soumallya Dey', 'Male', '21')
filepath = os.path.join(savePath, filename)
f = open(filepath, 'w+')
f.writelines('\nName: Soumallya Dey, Gender: Male, Age: 21\n')
f.close()
for line in file1:
    for i in range(len(string1)):
        if string1[i] in line:
            print(line)
            with open(filepath, '+a') as f:
                f.writelines(f'\n{line}')
                f.close()
            break

