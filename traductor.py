#pip install SpeechRecognition

import speech_recognition as sr

def transcribir_google(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        return texto
    except sr.UnknownValueError:
        return "No se pudo entender el audio"
    except sr.RequestError:
        return "Error de conexión con Google API"

#audio_file = "audio2.wav"
text=transcribir_google("audio2.wav")
with open("archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write(text)