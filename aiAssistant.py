# This module makes the Assistance to speak
import pyttsx3
import datetime
import speech_recognition as sr
from sympy import EX
import wikipedia
import webbrowser
import os
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
chromePath = r'C:\Program Files\Google\Chrome\Application\chrome.exe%s'
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromePath))
browser = webbrowser.get('chrome')
engine = pyttsx3.init('sapi5') #sapi5 is Microsoft's speech API
# print(voices)
# print(engine)
# print(voices[0].id)
# print(voices[1].id)
# Female Voice isn't working. Even if I change the index to one.
voices = engine.getProperty('voices') # There already exists two voices. One male and female 
engine.setProperty('voice',voices[0].id)
chVoice = 1
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Greetings():
    hour = datetime.datetime.now().hour
    if hour>= 0 and hour<= 12:
        speak('Good Morning!')
    elif hour >12 and hour < 16:
        speak("Good Afternoon")
    else :
        speak("Good Evening")

    speak("Hello , I'm your Desktop Voice Assistant. Please tell me how may I help you")

def takeCommand():
    '''
    This function converts the Voice given as input from the microphone to text 
    '''
    r = sr.Recognizer()
    print(sr.Microphone)
    with sr.Microphone() as source :
        print('Listening...')
        r.pause_threshold = 0.7 # Waits for 1sec until the statement is generated 
        audio = r.listen(source)
        # print(audio) 
    
    try:
        print('Recognizing ..')
        query = r.recognize_google(audio, language='en-in')
        print(f'The user said : {query}')

    except Exception as e:
        print(e)
        print('Cannot be recognized. Could you repeat it please')
        return "None"
    return query
if __name__ == '__main__':
    Greetings()
    while True:
        query = takeCommand().lower()
        print(query)
        # Executing queries
        # Improv by selenium needed
        if 'open' in query:
            if 'youtube' in query:
                speak('Opening Youtube')
                # webbrowser.get(r'C:\Program Files\Google\Chrome\Application\chrome.exe').open('youtube.com')
                webbrowser.open_new_tab('youtube.com')
            elif 'google' in query:
                browser.open('google.com')
            elif 'instagram' in query:
                browser.open('instagram.com')
            elif 'code' in query:
                speak('opening Vs code')
                codePath = r'"C:\Users\admin\AppData\Local\Programs\Microsoft VS Code\Code.exe"'
                os.startfile(os.path.join(codePath))
            elif 'spotify' in query:
                try:
                    speak('Opening spotify')
                    path = r'C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.181.604.0_x86__zpdnekdrzrea0\Spotify.exe'
                    os.startfile(os.path.join(path))
                except Exception as e:
                    print(e)
                    speak('cannot open spotify')

        elif 'play music' in query:
            musicPath = r'C:\Users\admin\Music'
            songs = os.listdir(musicPath)
            print(songs)
            # ran = random
            os.startfile(os.path.join(musicPath, songs[0]))


        elif 'wikipedia' in query:
            # print("why is this being executed")
            speak('Searching in Wikipedia')
            query = query.replace('wikipedia', '')
            print(query)
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak('According to Wikipedia')
            speak(results)

        elif 'door' in query:
            if ('check' or 'who is') in query:
                try:
                    speak('Checking')
                    webbrowser.open('')
                except Exception as e:
                    speak('Camera is not working')
                    print(e)

        elif ('who is' or 'what is') in query:
            speak('Searching in Wikipedia')
            query = query.replace('who is', '')
            query = query.replace('what is', '')
            print(query)
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif 'change your voice' in query:
            engine.setProperty('voice', voices[chVoice].id)
            chVoice = 0
            speak('Hello')
        



