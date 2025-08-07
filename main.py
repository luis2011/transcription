#pip install SpeechRecognition
import speech_recognition as sr
from moviepy import VideoFileClip
#from moviepy.editor import VideoFileClip
import whisper

# Función para extraer el audio de un video
def extraer_audio(video_path, audio_output):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_output)

# Función para transcribir el audio usando Whisper
def transcribir_audio(audio_path, modelo='base'):
    model = whisper.load_model(modelo)
    result = model.transcribe(audio_path)
    return result['text']

# Ruta del archivo de video y nombre del archivo de audio intermedio
video_path = "video.mp4"      # Cambiar por la ruta del video
audio_path = "audio.wav"      # Archivo temporal de audio

# Proceso completo: extraer audio y transcribir
extraer_audio(video_path, audio_path)
#texto_transcripto = transcribir_audio(audio_path)

# Mostrar resultado
print("Transcripción del audio:")
#print(texto_transcripto)

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
text=transcribir_google("audio.wav")
with open("archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write(text)