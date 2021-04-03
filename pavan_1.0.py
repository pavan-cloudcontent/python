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

speak("Welcome, Bubbu")
time_()