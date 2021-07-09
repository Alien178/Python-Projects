import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import time
import pyjokes

global hour
hour = None

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("My name is Jarvis. How may I help you")       

def takeCommand():
    stopCount = 0

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")
        stopCount += 1
        if stopCount >= 5:
            speak("Cannot Understand")
            time.sleep(1)
            quit()
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")   

        elif "search on google" in query:
            google = query.replace("search on google", "")
            pywhatkit.search(google)
            speak("Seearching" + google + "on web")

        elif "play" in query:
            play = query.replace("play", "")
            speak("playing" + play)
            pywhatkit.playonyt(play)

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {strTime}")

        elif "stop" in query:
            quit()

        elif "joke" in query:
            joke = pyjokes.get_joke("en")
            speak(joke)

        elif "help" in query:
            speak("My Commands are")
            time.sleep(0.5)
            speak("To Play Certain Things on Youtube")
            time.sleep(0.5)
            speak("To Open Stackflow")
            time.sleep(0.5)
            speak("To Search on Wikipedia")
            time.sleep(0.5)
            speak("To Search on Google")
            time.sleep(0.5)
            speak("To Tell Time")
            time.sleep(0.5)
            speak("To Tell a Joke")
            time.sleep(0.5)
            speak("To Quit Program")
