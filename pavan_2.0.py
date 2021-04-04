import pyttsx3 # pip install pyttsx3
import datetime
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is :")
    speak(Time)

def date_():
    year=str(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    day=str(datetime.datetime.now().day)
    speak("The current date is")
    speak(year)
    speak(month)
    speak(day)
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning Bubbu")
    elif hour>=12 and hour<=18:
        speak("Good Evening Bubbu")
    elif hour>18 and hour <= 24:
        speak("Good evening Bubbu") 
    else:
        speak("Good Night") 
def welcome_():
    speak("Welcome, Bubbu")
    time_()
    date_()

welcome_()