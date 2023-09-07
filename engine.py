import pyttsx3
import speech_recognition as sr
import sys
import os
from urllib.request import urlopen
from googletrans import Translator

text = ''
print('\033[1;31;40m AutoTranslate by Tayzar02. Built with <3 off the back of https://github.com/Tayzar02/JARVIS\n')
translator = Translator(service_urls=['translate.google.com','translate.google.co.kr',])
def talk(text):
		engine = pyttsx3.init()
		rate = engine.getProperty('rate')
		engine.setProperty('rate', rate-50)
		voices = engine.getProperty('voices')
		engine.setProperty('voice', voices[1].id)
		engine.say(text)
		engine.runAndWait()

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""
	
		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exception: "+ str(e))
	return said.lower()
	
def translate(text):
    result = translator.translate(text, dest='en')
    return result.text

while 'Stop Translating' not in text:
	print('\033[1;31;40m AutoTranslate ready!\n')
	text = get_audio()
	
	print(translate(text))
sys.exit()