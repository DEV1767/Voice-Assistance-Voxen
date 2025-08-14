import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  
    engine.say(audio)
    engine.runAndWait()
      

#Basic For wishing 
def time():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning!")
        print("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak("Good Evening!")
        print("Good Evening!")


#normal Greeting lines
def Greeting():
  speak("Namasta am Voxen build using Python i can perform some basic task wright now So how can I help you ? ")

def intro():
    speak(" I am Voxen means one with a voice and i am your personal voice assistant, created by Shivam using Python. I can understand and speak in both English and Hindi, recognize your voice, answer your questions, and help you with daily tasks.")
 #For taking task from using 
def task():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("You can speak, I am listening, don’t worry...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  
        print(f'You said: {query}\n')

    except Exception as e:
        print(e)
        print("Speak again")
        query = None

    return query


#Main Function

if __name__ == "__main__":
    time()
    Greeting()
    while True:
        Query = task()
        if Query:
            Query = Query.lower()
        else:
            continue

        if 'google' in Query:
            speak("Ok sir i will open Google for you")
            webbrowser.open('https://www.google.com/')

        elif 'introduce yourself' in Query:
            intro()

        elif 'open youtube' in Query:
            speak("Ok sir i will open youtube for you")
            webbrowser.open('https://www.youtube.com/')

        elif 'open my github' in Query:
            speak("Ok sir i will open Github for you")
            webbrowser.open('https://github.com/DEV1767')

        elif 'open my linkedin' in Query:
            speak("Ok sir i will open Linkedin for you") 
            webbrowser.open('https://www.linkedin.com/in/shivam076/')

        elif 'open my college account' in Query:
            speak("This will require you College USN number and PassWord to login First Go to student and then enter all detail your usn number and password and For parents login  enter your parents phone number")
            webbrowser.open('https://jams-jnnce.in/')

        elif 'open whatsapp' in Query:
          webbrowser.open('https://web.whatsapp.com/')
