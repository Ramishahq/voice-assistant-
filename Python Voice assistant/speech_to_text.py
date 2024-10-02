#pip install SpeechRecognition 
#pip install PyAudio



import speech_recognition as sr
r = sr. Recognizer()
def listen():
    with sr.Microphone() as source: 
        print("listening")
        audio = r.listen(source)
        text = r.recognize_google(audio)

        print(text)
        return text
    
    