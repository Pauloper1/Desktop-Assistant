# This module makes the Assistance to speak
import pyttsx3
import datetime
import speech_recognition as sr
from sympy import EX
import wikipedia
import webbrowser
import os
import wolframalpha

#--------------------------
#application Paths and required urls 
#--------------------------

# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
chromePath = r'C:\Program Files\Google\Chrome\Application\chrome.exe%s'
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chromePath))
browser = webbrowser.get('chrome')
engine = pyttsx3.init('sapi5') #sapi5 is Microsoft's speech API

voices = engine.getProperty('voices') # There exists two voices. One male and female 
engine.setProperty('voice',voices[0].id) # Note : while getting the properties its 'voices' and while setting the properties its 'voice'

chVoice = 1
#---------------------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#--------------------------

def Greetings():
    hour = datetime.datetime.now().hour
    if hour>= 0 and hour<= 12:
        speak('Good Morning!')
    elif hour >12 and hour < 16:
        speak("Good Afternoon")
    else :
        speak("Good Evening")

    speak("Hello , I'm your Desktop Voice Assistant,Eren. Please tell me how may I help you") 
        

#--------------------------

def takeCommand():
    '''
    This function converts the given speech as input from the microphone to text 
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

#--------------------------


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
                webbrowser.open('google.com')
            elif 'instagram' in query:
                webbrowser.open('instagram.com')
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
            elif 'facebook' in query:
                try:
                    speak('Opening facebook')
                    webbrowser.open('facebook.com')
                except Exception as e:
                    print(e)
                    speak('cannot open facebook')


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
                url = '192.168.43.184'
                try:
                    speak('Checking')
                    webbrowser.open(url)
                except Exception as e:
                    speak('Camera is not working')
                    print(e)

        # elif ('who is' or 'what is') in query:
        #     speak('Searching in Wikipedia')
        #     query = query.replace('who is', '')
        #     query = query.replace('what is', '')
        #     print(query)
        #     results = wikipedia.summary(query, sentences=2)
        #     print(results)
        #     speak(results)

        elif ('change your voice' or 'character')in query:
            engine.setProperty('voice', voices[chVoice].id)
            chVoice = 1 if chVoice == 0 else 0
            speak("Hello , I'm your Desktop Voice Assistant,Maarin. Please tell me how may I help you")

        elif ('calculate' or 'weather' or 'what is')in query:
            appId = 'JRGY87-5G9AXR6K5L'
            client = wolframalpha.Client(appId)
            # indx = query.lower().split().index('calculate')
            # print(indx)
            # speak('helo')
            # query = query.split()[indx + 1:]
            # print(query)
            res = client.query(query)
            print(res)
            answer = next(res.results).text
            speak('The answer is '+ answer)
            print(answer)




