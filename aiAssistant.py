# This module makes the Assistance to speak
from numpy import chararray
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


chromePath = r'C:\Program Files\Google\Chrome\Application\chrome.exe%s'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
browser = webbrowser.get('chrome')
engine = pyttsx3.init('sapi5')  # sapi5 is Microsoft's speech API

# There are two voices. One male and female
voices = engine.getProperty('voices')
# Note : while getting the properties its 'voices' and while setting the properties its 'voice'
engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 200)


class queries:

    def __init__(self):
        self.engine = engine
        self.chVoice = 1
        self.greetOnce = True
#---------------------------

    def speak(self, audio):
        self.tempAudio = audio
        engine.say(audio)
        engine.runAndWait()

    #--------------------------

    def ChangeVoice(self, a):
        if(a == 'Maarin'):
            self.chVoice = 1
        elif (a == 'Eren'):
            self.chVoice = 0

        engine.setProperty('voice', voices[self.chVoice])

    def Greetings(self):
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour <= 12:
            self.speak('Good Morning!')
        elif hour > 12 and hour < 16:
            self.speak("Good Afternoon")
        else:
            self.speak("Good Evening")

        self.speak(
            "Hello , I'm your Desktop Voice Assistant,Eren. Please tell me how may I help you")

    #--------------------------

    def takeCommand(self):
        '''
        This function converts the given speech as input from the microphone to text 
        '''
        self.r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print('Listening...')
            # self.r.pause_threshold = 0.7  # Waits for 1sec until the statement is generated
            self.audio = self.r.listen(source)

        try:
            print('Recognizing ..')
            self.query = self.r.recognize_google(self.audio, language='en-in')
            print(f'The user said : {self.query}')

        except Exception as e:
            print(e)
            print('Cannot be recognized. Could you repeat it please')
            return "None"
        return self.query

    #--------------------------

    def Convo(self):
        self.res = ''
        if self.greetOnce == True:
            print(self.greetOnce)
            self.Greetings()
            self.greetOnce = False
            print(self.greetOnce)

        self.query = self.takeCommand().lower()
        print(self.query)
        # Executing queries
        # Improv by selenium needed

        #Basic Opening Operations
        if 'open' in self.query:

            if 'youtube' in self.query:
                self.res = 'Opening Youtube'

                webbrowser.open_new_tab('youtube.com')
            elif 'google' in self.query:
                webbrowser.open('google.com')

            elif 'instagram' in self.query:
                self.res = 'Opening Instagram'
                webbrowser.open('Instagram.com')

            elif 'code' in self.query:
                self.speak('opening Vs code')
                codePath = r'"C:\Users\admin\AppData\Local\Programs\Microsft VS Code\Code.exe"'
                os.startfile(os.path.join(codePath))
            elif 'spotify' in self.query:
                try:
                    self.speak('Opening spotify')
                    path = r'C:\ProgramFiles\WindowsApps\SpotifyAB.SpotifyMusic_1181.604.0_x86__zpdnekdrzrea0\Spotify.exe'
                    os.startfile(os.path.join(path))
                except Exception as e:
                    print(e)
                    self.speak('cannot open spotify')
            elif 'facebook' in self.query:
                try:
                    self.speak('Opening facebook')
                    webbrowser.open('facebook.com')
                except Exception as e:
                    print(e)
                    self.speak('cannot open facebook')
        elif 'play music' in self.query:
            musicPath = r'C:\Users\admin\Music'
            songs = os.listdir(musicPath)
            print(songs)
            os.startfile(os.path.join(musicPath, songs[0]))

        elif 'wikipedia' in self.query:
            try:
                self.speak('Searching in Wikipedia')
                self.query = self.query.replace('wikipedia', '')
                print(self.query)
                self.res = wikipedia.summary(self.query, sentences=1)
            except:
                self.res = 'Cannot process the query'

        elif 'door' in self.query:
            if ('check' or 'who is') in self.query:
                url = '192.168.43.184:81/stream'
                try:
                    self.speak('Checking')
                    webbrowser.open(url)
                except Exception as e:
                    self.speak('Camera is not working')
                    print(e)
        elif ('change your voice' or 'character') in self.query:
            try:
                engine.setProperty('voice', voices[self.chVoice].id)
                self.chVoice = 1 if self.chVoice == 0 else 0
                characterV = ''
                if self.chVoice == 0:
                    characterV = 'Maarin'
                else:
                    characterV = 'Eren'
                self.res = f"Hello , I'm your Desktop VoiceAssistant, Maarin. Please tell me how may I help you"
            except:
                self.res = 'Cannot process the query'

        elif 'who is ' in self.query or 'calculate' in self.query or 'weather' in self.query or 'what is' in self.query:
            try:
                # The queries for wolframalpha has a limit up to 2000 queries only.
                # So if it gets exhausted, go to wolframalpha and get your appID.
                # https: // products.wolframalpha.com/simple-api/documentation/ -> for appId
                appId = 'Your appId'
                client = wolframalpha.Client(appId)
                res = client.query(self.query)
                self.res = next(res.results).text
                self.res = 'The answer is ' + self.res
            except:
                self.res = 'Cannot process the query'

        elif 'introduce yourself' in self.query or 'who are you' in self.query:
            characterV = ''
            if self.chVoice == 0:
                characterV = 'Maarin'
            else:
                characterV = 'Eren'

            self.res = f'Hello ,I am {characterV} , Desktop Voice Assistant, developed by Paul,Justin and Karthik'
