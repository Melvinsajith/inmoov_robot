import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndwait()

if __name__ == "__main__":
    speak("harry is a good boy")
