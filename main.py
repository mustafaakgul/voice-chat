from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language='tr-TR') #'tr'
        except sr.UnknownValueError:
            speak('Anlamadım')
        except sr.RequestError:
            speak('Servis çalışmıyor')
        return voice_data

"""
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language='tr')
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, my speech service is down')
        return voice_data
"""

def speak(text):
    tts = gTTS(text=text, lang='tr') # lang='en' for english, tr for turkish
    file = 'voice.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

def response(voice):
    if 'merhaba' in voice:
        speak('Sanada merhaba genç')
    if 'nasılsın' in voice:
        speak('İyiyim sen nasılsın')

speak("Ben Darb")

while True:
    voice = record_audio()
    if voice != '':
        voice = voice.lower()
        print(voice)
        response(voice)
    else:
        print("No voice")
