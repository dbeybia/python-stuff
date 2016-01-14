import pyttsx
from random import randint


name = raw_input("Say something dirty and the it will say something dirty back :)\n")

file_object = open("list.txt", "r")
lines = file_object.readlines()

def callback():
	engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0') 
	randomline = randint(0,len(lines))
	x = lines[randomline]
	engine.say(x)
	engine.runAndWait()
	
	
engine = pyttsx.init()

callback()

raw_input("")