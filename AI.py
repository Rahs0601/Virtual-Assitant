import streamlit as st
import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import time
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)
    return 0

def reco():
    try:
        res = ''
        with sr.Microphone() as source:
            st.write('Listening...')
            voice = listener.listen(source)
            res = listener.recognize_google(voice)
            res = res.lower()
            st.write(res)
    except:
        talk('Error')
    return res

def action(command):
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time1 = datetime.datetime.now().strftime('%I %M %p')
        st.write(time1)
        talk('Currently in india its' + time1)
    
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 2)
        st.write(info)
        talk(info)
    else:
        google = command.replace('search', '')
        pywhatkit.search(google)
        talk('I found this on google')
    return 0

st.title('Virtual Assistant')
st.write('Heya...!, this is Rah\'s virtual assistant')
st.write('Built to work as an AI')
st.write('How can I help you')

command = st.text_input('Enter a command')

if st.button('Submit'):
    action(command)
    talk('Thank you')
