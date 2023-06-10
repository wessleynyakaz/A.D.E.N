'''
Defines the output and input of sound
'''
MALE = 0
FEMALE = 1

def speak(words: str):
    from  pyttsx3 import init
    aden = init()
    voices = aden.getProperty('voices')
    aden.setProperty('rate', 190)
    aden.setProperty('volume', 1.0)
    aden.setProperty('voice', voices[FEMALE].id)
    aden.say(words)
    aden.runAndWait()