# Import All Important Modules.
import pyttsx3
import speech_recognition as sr
import os

engine = pyttsx3.init()


# Create a function for output the voice from machine.
def speak(text):
    engine.say(text)
    engine.runAndWait()


speak('Initializing your system sir...')


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


# Create a function 'Name' which is taking Patient Name from user.
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


# Create a function 'Name' which is taking Patient Name from user.
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
    try:
        if 'start' in query:
            r5 = sr.Recognizer()
            PatientName = name()
            Gender = gender()
            Age = age()
            Address = input("What is the address:")
            mobileNumber = int(input("Enter Patient mobile number: "))
            emailId = input("What is the Email Address: ")
            savePath = 'D:\\project\\Prescription\\NewFiles\\'
            filename = '%s_%s_%s_0.txt' % (PatientName, Gender, Age)
            filepath = os.path.join(savePath, filename)
            f = open(filepath, 'w+')
            f.writelines(
                f'PatientName: {PatientName}, Gender: {Gender}, Age: {Age}\n')
            f.close()
            while True:
                with sr.Microphone() as source5:
                    try:
                        r5.adjust_for_ambient_noise(source5)
                        print("Which items you want to add")
                        speak("Which items you want to add")
                        audio_text = r5.listen(source5)
                        query2 = r5.recognize_google(audio_text, language='en-in')
                        if 'complete' in query2:
                            break
                        else:
                            for line in r5.recognize_google(audio_text):
                                print(line)
                                medicine.append(line)
                            with open(filepath, '+a') as f:
                                f.writelines(f'\n{medicine}')
                                f.close()
                                medicine.clear()
                            print("This is saved, thanks")
                            speak("This is saved, thanks")
                    except Exception as e:
                        print(e)
    except Exception as e:
        print(e)
