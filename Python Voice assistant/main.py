from text_to_speech import speak
from speech_to_text import listen 


speak("Hello, I am your Voice Assistant today. How can I help you")

text= listen()
print(text)
