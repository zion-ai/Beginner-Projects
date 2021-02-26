import speech_recognition as sr 
from datetime import datetime
import time
import webbrowser
from gtts import gTTS 
from playsound import playsound
import random 
import os


r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        auido = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(auido, language='tr-TR', show_all=True)
        except sr.UnknownValueError:
            speak('Anlayamadım!')
        except sr.RequestError:
            speak('sistem çalışmıyor')
        return voice

def response(voice):
    if 'nasılsın' in voice:
        speak('İyi senden')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('Ne aramak istiyorsun?')
        url= 'https://google.com/search?='+search
        webbrowser.get().open(url)
        speak(search+' için bulduklarım.')
    if 'tamamdır' in voice:
        speak('görüşürüz!')
        exit()


def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('nasıl yardımcı olabilirim')
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)