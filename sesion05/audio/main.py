from gtts import gTTS
import os

texto = input('Escriba un texto a convertir: ')
tts = gTTS(text=texto,lang='es')
filename = 'texto_convertido.mp3'
tts.save(filename)
os.system(f'start {filename}')