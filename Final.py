# Import All Important Modules.
import pyttsx3
import datetime
import speech_recognition as sr
from PyPDF2 import PdfFileMerger
from fpdf import FPDF
from mysql.connector import connect
import time
import os
import pytesseract
from PIL import Image
from AttacthmentMail import sendmail

engine = pyttsx3.init()  # Make a engine variable for transferring voices.
mydb = connect(host="localhost", user="root", database="studentdate")  # Create a connect between user and database.
mycursor = mydb.cursor()  # Cursor is a control structure used to traverse and fetch the records of the database
mycursor.execute("select * from `student details`")
result = mycursor.fetchall()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
path = 'D:\\project\\Prescription\\Images'
mkdir = os.listdir(path)


# Create a function for output the voice from machine.
def speak(text):
    engine.say(text)
    engine.runAndWait()


# speak('Initializing your system sir...')


# Create a function 'takecommand' which is taking query from user.
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print('listening...')
            speak('listening...')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"user said:{query}\n")
        except Exception as e:
            print('Say that again please')
            query = None
    return query


# Create a function 'Name' which is taking Patient Name from user.
def name():
    r1 = sr.Recognizer()
    with sr.Microphone() as source1:
        try:
            speak("What is the name of this Patient")
            print("What is the name of this Patient")
            r1.adjust_for_ambient_noise(source1)
            audio1 = r1.listen(source1)
            Nameis = r1.recognize_google(audio1, language='en-in')
            print(f'Name is:{Nameis}\n')
            speak(f'Name is:{Nameis}\n')
        except Exception as e:
            print(e)
            speak('Please say again')
    return Nameis.lower()


# Create a function 'Gender' which is taking Patient Gender from user.
def gender():
    r2 = sr.Recognizer()
    with sr.Microphone() as source2:
        try:
            speak("What is the gender of this Patient")
            print("What is the gender of this Patient")
            r2.adjust_for_ambient_noise(source2)
            audio1 = r2.listen(source2)
            Genderis = r2.recognize_google(audio1, language='en-in')
            print(f'Gender is:{Genderis}\n')
            speak(f'Gender is:{Genderis}\n')
        except Exception as e:
            speak('Please say again')
    return Genderis


# Create a function 'age' which is taking Patient Age from user.
def age():
    r3 = sr.Recognizer()
    with sr.Microphone() as source3:
        try:
            speak("What is the age of this Patient")
            print("What is the age of this Patient")
            r3.adjust_for_ambient_noise(source3)
            audio1 = r3.listen(source3)
            ageis = r3.recognize_google(audio1, language='en-in')
            print(f'Gender is:{ageis}\n')
            speak(f'Gender is:{ageis}\n')
        except Exception as e:
            speak('Please say again')
    return ageis


# Image text's store in a txt file
def ImageToText(filePath):
    for filename in mkdir:
        filelocation = (path, filename)
        myfile = '\\'.join(filelocation)
        img = Image.open(myfile)
        text = pytesseract.image_to_string(img)
        with open(filePath, '+a') as f:
            f.writelines(f'{text}')
            f.close()
        os.remove(filename)
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=11)
        f = open(filePath, "r")
        for x in f:
            pdf.cell(200, 10, txt=x, ln=1, align='C')
        PdfFile = pdf.output("Pathology.pdf")
        return PdfFile
    except Exception as e:
        print(e)


# Convert Txt To pdf File
def TexToPdf(filename):
    try:
        count = 0
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=11)
        f = open(filename, "r")
        for x in f:
            pdf.cell(200, 10, txt=x, ln=1, align='C')
        OtherPdfFile = pdf.output(f"{ID}{count}.pdf")
        count += 1
        return OtherPdfFile
    except Exception as e:
        print(e)


# Marging All pdf files
def pdf_merger(name, filepath, filepath1, filepath2):
    try:
        pdfs = [filepath, filepath1, filepath2]
        merger = PdfFileMerger()
        for pdf in pdfs:
            print("merging")
            merger.append(pdf)
        finalfile = f"D:\\project\\Prescription\\PrescriptionImage\\{name}.pdf"
        merger.write(f"{finalfile}")
        print("merge successful")
        merger.close()
        return finalfile
    except Exception as e:
        print(e)


# Convert  proper format to binary data and read it on Database
def read_file(filepath):
    with open(filepath, 'rb') as file:
        binarydata = file.read()
    return binarydata


# Convert binary data to proper format and write it on Hard Disk
def write_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)


medicine = []
medicine1 = []
ID = None
file1 = None
file2 = None
file3 = None
while True:
    query = takeCommand()
    try:
        if 'create' in query:
            PatientName = name()
            Gender = gender()
            Age = age()
            ver = PatientName.split()
            arivaltime = str(int(time.time()))
            UniqueIDCreate = (arivaltime + ver[0][0] + ver[1][0])
            Address = input("What is the address:")
            mobileNumber = int(input("Enter Patient mobile number: "))
            emailId = input("What is the Email Address: ")
            ID = UniqueIDCreate
            sql = "insert into `student details`(ID,Name, Sex, Age, Address, `Mobile No`, `Email Id`) values (%s ," \
                  "%s, %s, %s, %s, %s) "
            val = (UniqueIDCreate, PatientName, Gender, Age, Address, mobileNumber, emailId)
            mycursor.execute(sql, val)
        elif 'report' in query:
            speak('Please enter Patient UniqueID')
            UniqueID = input('Please enter Patient UniqueID')
            ID = UniqueID
            for value in result:
                if UniqueID == value[0]:
                    report = value[7]
                    ReportFileName = f'PrescriptionImage\\{UniqueID}.pdf'
                    write_file(report, ReportFileName)
        elif 'path' in query:
            mycursor1 = mydb.cursor()
            mycursor1.execute("select * from `student details`")
            result1 = mycursor1.fetchall()
            for value1 in result1:
                if ID == value1[0]:
                    day = datetime.datetime.now().day
                    month = datetime.datetime.now().month
                    year = datetime.datetime.now().year
                    savePath = 'D:\\project\\Prescription\\NewFiles\\'
                    filename = '%s_%s_%s_Pathology.txt' % (value1[1], value1[2], value1[3])
                    filepath = os.path.join(savePath, filename)
                    f = open(filepath, 'w+')
                    f.writelines(
                        f'PatientName: {value1[1]}, Gender: {value1[2]}, Age: {value1[3]}, day: {day}, month: {month}, year: {year}\n')
                    f.close()
                    file1 = ImageToText(filepath)
                    print('Success')
        elif 'dia' in query:
            mycursor2 = mydb.cursor()
            mycursor2.execute("select * from `student details`")
            result2 = mycursor2.fetchall()
            for value2 in result2:
                if ID == value2[0]:
                    day = datetime.datetime.now().day
                    month = datetime.datetime.now().month
                    year = datetime.datetime.now().year
                    savePath = 'D:\\project\\Prescription\\NewFiles\\'
                    filename = '%s_%s_%s_Pathology.txt' % (value2[1], value2[2], value2[3])
                    filepath1 = os.path.join(savePath, filename)
                    f = open(filepath1, 'w+')
                    f.writelines(
                        f'PatientName: {value2[1]}, Gender: {value2[2]}, Age: {value2[3]}, day: {day}, month: {month}, year: {year}\n')
                    f.close()
                    while True:
                        with sr.Microphone() as source4:
                            r3 = sr.Recognizer()
                            try:
                                r3.adjust_for_ambient_noise(source4)
                                print("Which items you want to add")
                                speak("Which items you want to add")
                                audio_text = r3.listen(source4)
                                query1 = r3.recognize_google(audio_text, language='en-in')
                                if 'complete' in query1:
                                    file2 = TexToPdf(filepath1)
                                    break
                                else:
                                    for line in r3.recognize_google(audio_text):
                                        medicine.append(line)
                                    with open(filepath1, '+a') as f:
                                        f.writelines(f'\n{medicine}')
                                        f.close()
                                        medicine.clear()
                                        print("This is saved, thanks")
                                        speak("This is saved, thanks")
                            except Exception as e:
                                print(e)
                                print("Sorry, I did not get that")
        elif 'medi' in query:
            mycursor3 = mydb.cursor()
            mycursor3.execute("select * from `student details`")
            result3 = mycursor3.fetchall()
            for value3 in result3:
                if ID == value3[0]:
                    day = datetime.datetime.now().day
                    month = datetime.datetime.now().month
                    year = datetime.datetime.now().year
                    savePath = 'D:\\project\\Prescription\\NewFiles\\'
                    filename = '%s_%s_%s_Pathology.txt' % (value3[1], value3[2], value3[3])
                    filepath2 = os.path.join(savePath, filename)
                    f = open(filepath2, 'w+')
                    f.writelines(
                        f'PatientName: {value3[1]}, Gender: {value3[2]}, Age: {value3[3]}, day: {day}, month: {month}, year: {year}\n')
                    f.close()
                    while True:
                        with sr.Microphone() as source4:
                            r4 = sr.Recognizer()
                            try:
                                r4.adjust_for_ambient_noise(source4)
                                print("Which items you want to add")
                                speak("Which items you want to add")
                                audio_text = r4.listen(source4)
                                query2 = r4.recognize_google(audio_text, language='en-in')
                                if 'complete' in query2:
                                    file3 = TexToPdf(filepath2)
                                    break
                                else:
                                    for line in r4.recognize_google(audio_text):
                                        medicine1.append(line)
                                    with open(filepath2, '+a') as f:
                                        f.writelines(f'\n{medicine1}')
                                        f.close()
                                        medicine1.clear()
                                        print("This is saved, thanks")
                                        speak("This is saved, thanks")
                            except Exception as e:
                                print(e)
                                print("Sorry, I did not get that")
        elif 'exit' in query:
            final = pdf_merger(ID, file1, file2, file3)
            mycursor4 = mydb.cursor()
            mycursor4.execute("select * from `student details`")
            result4 = mycursor4.fetchall()
            for value4 in result4:
                if ID == value4[0]:
                    query = "UPDATE `student details` SET report = %s WHERE id  = %s"
                    UpdateFile = input('Enter your file Path: ')
                    binaryfile = read_file(UpdateFile)
                    val = (binaryfile, ID)
                    sendmail(value4[6], final)
            break
    except Exception as e:
        print(e)

# 1631713849sd