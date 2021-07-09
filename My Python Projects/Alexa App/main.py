import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
command = ''



def talk(text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                command = command.replace('jarvis', '')

    except:
        pass

    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing song' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk("Current time is" + time)
        

    elif 'search on wiki' in command:
        person = command.replace('search on wiki', '')
        info = wikipedia.summary(person, 1)
        talk(info)

    elif 'search' in command:
        google = command.replace('search', '')
        pywhatkit.search(google)
        talk('Searching' + google + 'on web')

    elif 'joke' in command:
        joke = pyjokes.get_joke('en')
        talk(joke)

    elif 'stop listening' in command:
        talk('Stop to listen')
        exit()

    else:
        talk('I did not understand the command')

    

while True:
    run_alexa()

