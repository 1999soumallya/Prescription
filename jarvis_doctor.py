import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()

filename = ""


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


wishMe()
speak('Initializing jarvis sir...')
counter = 0

while True:
    query = takeCommand().lower()
    if 'start' in query:
        PatientName = input('Enter PatientName: ')
        Gender = input('Enter PatientGender:')
        Age = int(input('Enter PatientAge:'))
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        filename = '%s_%s_%s_%s_%s_%s.csv' % (PatientName, Gender, Age, day, month, year)
        f = open(filename, '+w')
        f.close()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Time over, thanks")
            try:
                with open(filename, '+') as f:
                    for line in r.recognize_google(audio_text):
                        f.writelines(f'{line}')
            except:
                print("Sorry, I did not get that")
                counter += 1

    elif counter >= 10:
        break
