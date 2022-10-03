import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    secound = int(datetime.datetime.now().second)
    print(hour, ':', minute, ':', secound)
    if 0 <= hour <= 12:
        engine.say('Good Morning')
    elif 12 < hour <= 17:
        engine.say('Good Afternoon')
    elif 17 < hour <= 20:
        engine.say('Good Evening')
    else:
        engine.say('Good night')
    print('Initializing jarvis sir...')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print('Say that again please')
        query = None
    return query


def csvcreaction():
    PatientName = input('Enter PatientName: ')
    Gender = input('Enter PatientGender:')
    Age = int(input('Enter PatientAge:'))
    file = '%s_%s_%s.csv' % (PatientName, Gender, Age)
    f = open(file, '+w')
    f.close()


def writePrescription(name):
    pass


wishMe()
speak('Initializing jarvis sir...')
while True:
    query = takeCommand().lower()
    if 'start' in query:
        csvcreaction()
    elif 'google' in query:
        speak('Opening Google...')
        webbrowser.open("google.com")
    elif 'quit' in query:
        exit(0)