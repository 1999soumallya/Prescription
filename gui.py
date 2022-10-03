from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import requests
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
import pytesseract
from PIL import Image
import os
import pyttsx3
import datetime
import speech_recognition as sr
import threading

filepath = 0



def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Image Files","*.png"),("all files","*.*")))
	global filepath
	filepath = filename
	label_file_explorer.configure(text="File Opened: "+filepath)	
	print(filepath)


def filecreate(text,name):
    file = '%s.txt' % (name)
    with open(file, '+a') as f:
        f.writelines(f'{text}')
        f.close()
	

def scan():

	try:		
		name = input('Enter your name: ')
		
		pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
		#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
		path = 'H:\\speech'
		#path = 'D:\\project\\PrectipctionImage\\Images'
		mkdir = os.listdir(path)
		for filename in mkdir:
			filelocation = (path, filename)
			myfile = '\\'.join(filelocation)
			img = Image.open(myfile)
			text = pytesseract.image_to_string(img)
			filecreate(text,name)

		#test_file = ocr_space_file(filename=filepath, language='pol') # pdf_converter()  # 
		#txt = json.loads(test_file)
		#print(test_file)
	except OSError as e:
		messagebox.showwarning(title=None, message="No such file or Directory")



def clear():
	global filepath
	filepath = ''


def startDiagnose():
	import Doctor


def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()



def pdf_converter():
	try:
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font("Arial", size = 15)
		f = open("textfile1.txt", "r")
		for x in f:
			pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
		pdf.output("mygfg.pdf")
	except OSError as e:
		messagebox.showwarning(title=None, message="No such file or Directory")



def pdf_merger():
	try:
		filename=filepath
		pdfs = [filename,filename]

		merger = PdfFileMerger()
	
		for pdf in pdfs:
			print("merging")
			merger.append(pdf)

		merger.write("H:/result.pdf")
		print("merge successful")
		merger.close()
	except OSError as e:
		messagebox.showwarning(title=None, message="No such file or Directory")





engine = pyttsx3.init()
#mydb = connect(host="localhost", user="root", database="studentdate")  # We connect the database
#mycursor = mydb.cursor()  # Fetch all data from database


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak('Initializing your system sir...')


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
            speak('Please say again')
    return Nameis.lower()


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


def age():
    r3 = sr.Recognizer()
    with sr.Microphone() as source3:
        try:
            speak("What is the gender of this Patient")
            print("What is the gender of this Patient")
            r3.adjust_for_ambient_noise(source3)
            audio1 = r3.listen(source3)
            Genderis = r3.recognize_google(audio1, language='en-in')
            print(f'Gender is:{Genderis}\n')
            speak(f'Gender is:{Genderis}\n')
        except Exception as e:
            speak('Please say again')


counter = 0
i = 0

def voiceRec():
	while True:
		query = takeCommand().lower()
		if 'exit' in query:
			break

		elif 'start' in query:
			PatientName = name()
			Gender = gender()
			Age = age()
			day = datetime.datetime.now().day
			month = datetime.datetime.now().month
			year = datetime.datetime.now().year
			filename = '%s_%s_%s_%s_%s_%s.csv' % (PatientName, Gender, Age, day, month, year)
			f = open(filename, '+w')
			f.writelines(
				f'\n PatientName: {PatientName}, Gender: {Gender}, Age: {Age}, day: {day}, month: {month}, year: {year}')
			f.close()
			r4 = sr.Recognizer()
			while True:
				with sr.Microphone() as source4:
					r4.adjust_for_ambient_noise(source4)
					print("Which items you want to add")
					speak("Which items you want to add")
					audio_text = r4.listen(source4)
					try:
						query1 = r4.recognize_google(audio_text, language='en-in')
						if 'break' in query1:
							break
						else:
							with open(filename, '+w') as f:
								for line in r4.recognize_google(audio_text):
									f.writelines(f'{line}')
									print("This is saved, thanks")
									speak("This is saved, thanks")
						i += 1
					except:
						print("Sorry, I did not get that")
						


def start():
    print("starting voice thread ")
    t1 = threading.Thread(target=voiceRec)
    t1.start()
    print("started voice thread")
  

def stop():
    global stop_threads
    stop_threads = True
    print("stopping voice")

# API f5.56@yandex.com f5.56@yandex.comA rapidapi
		
# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("600x600")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,text = "File Explorer using Tkinter",width = 100, height = 4,fg = "blue")

	

button_explore = Button(window,text = "Browse Files",command = browseFiles)
button_scan = Button(window,text = "Scan Files",command = scan)
button_start = Button(window, text="Start Scan", command=start)
button_stop = Button(window, text="Stop", command=stop)
button_diagnose = Button(window,text = "Start Diagnose",command = startDiagnose)
button_medicine = Button(window,text = "Start Medicine",command = browseFiles)
button_convert = Button(window,text = "PDF Convert",command = pdf_converter)
button_merge = Button(window,text = "PDF Merge",command = pdf_merger)
button_clr = Button(window,text = "Clear",command = clear)
button_exit = Button(window,text = "Exit",command = exit)


label_file_explorer.grid(column = 1, row = 1)
button_start.grid(column = 1, row = 2)
button_stop.grid(column = 1, row = 3)
button_explore.grid(column = 1, row = 4)
button_scan.grid(column = 1,row = 5)
button_diagnose.grid(column = 1,row = 6)
button_medicine.grid(column = 1,row = 7)
button_convert.grid(column = 1, row = 8)
button_merge.grid(column = 1, row = 9)
button_clr.grid(column = 1, row = 10)
button_exit.grid(column = 1,row = 11)
# Let the window wait for any events
window.mainloop()