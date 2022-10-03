import pyttsx3
import datetime
import speech_recognition as sr
from mysql.connector import connect

engine = pyttsx3.init()
mydb = connect(host="localhost", user="root", database="studentdate")  # We connect the database
mycursor = mydb.cursor()  # Fetch all data from database


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
    return Genderis


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


medicine = []

while True:
    query = takeCommand()
    if 'start' in query:
        PatientName = name()
        Gender = gender()
        Age = age()
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        r4 = sr.Recognizer()
        filename = '%s_%s_%s_%s_%s_%s.txt' % (PatientName, Gender, Age, day, month, year)
        f = open(filename, 'w+')
        f.writelines(
            f'\n PatientName: {PatientName}, Gender: {Gender}, Age: {Age}, day: {day}, month: {month}, year: {year}')
        f.close()
        while True:
            with sr.Microphone() as source4:
                try:
                    r4.adjust_for_ambient_noise(source4)
                    print("Which items you want to add")
                    speak("Which items you want to add")
                    audio_text = r4.listen(source4)
                    query1 = r4.recognize_google(audio_text, language='en-in')
                    if 'complete' in query1:
                        break
                    else:
                        for line in r4.recognize_google(audio_text):
                            medicine.append(line)
                        with open(filename, '+r') as f:
                            f.writelines(f'\n{medicine}')
                            f.close()
                            medicine.clear()
                            print("This is saved, thanks")
                            speak("This is saved, thanks")
                except Exception as e:
                    print("Sorry, I did not get that")
    elif 'Handover' in query:
        break
