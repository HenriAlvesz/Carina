from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core
# Síntese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json

# Síntese de fala
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Reconhecimento de fala
model = Model('C:/Users/Alexssandra Bezerra/OneDrive/Desktop/Carina/Carina/model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()

while True:
    data = stream.read(1024)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if 'text' in result and result['text']:  # Verifique se a chave 'text' existe
            text = result['text']
            print(text)
            speak(text)

            if text == 'que horas':
                speak(core.SystemInfo.get_time())