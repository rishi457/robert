import pyttsx3 as p
from datetime import datetime as d
from speech_recognition import Recognizer as R, Microphone as m
from webbrowser import open as o
from time import sleep
from googlesearch import search as s
from webbrowser import open
import google as g
engine = p.init('sapi5')
voices = engine.getProperty('voices')

voices = engine.setProperty('voice', voices[0].id)
def say(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(d.now().hour)
    if hour >= 0 and hour < 12:
        say("good morning my friend")
    elif hour >= 12 and hour <18:
        say('Good afternoon ny friend')
    elif hour >= 18 and hour <21:
        say('Good evening ny friend')
    else:
        say("Good night my friend")
    say("it\'s robert in your service")
    say('how may i help you')
def listen():
    #It takes microphone input from the user and returns string output

         
    r = R()
    with m() as source:
        say("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
            say("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            say(f"User said: {query}\n")  #User query will be printed.
        except Exception as e:
            say("please try again...")   #please try again will be printed in case of improper voice
             
        if query.lower() == 'who made you':
            say('My honourable master     Sidhant made me')
        elif 'made' in query.lower():
            say('I was made as minor project by my honourable master Sidhant')
        elif 'google' in query.lower():
            q = query.replace('on google', '')
            new = 2
    
            say('opening google')
            
            for j in s(q, tld="com", num=1, stop=1, pause=2):
                g.open(f'{j}')
             

        elif 'youtube' in query.lower():
            open('www.youtube.com')

        elif 'classroom' in query:
            print('opening classroom')
            open('www.classroom.com')
        elif 'quit' in query.lower() or query.lower() == '':
            say('closing program')
            break
        
        elif ' open facebook' in query.lower():
            say('opening facebook')
            wb.open(www.facebook.com)
        elif 'quit' in query.lower():
            say('closing program')
            break
if __name__ == '__main__':
    wishMe()
    listen()
