#import
import pyttsx3 as p

engine = p.init()
#engine.say("Hello World")
#engine.runAndWait()

#SPEED AND VOICE
engine.setProperty("rate",180)
#voices = engine.getProperty('voices')
#print(voices)
#engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("Hello")