import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        recorded_audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(recorded_audio, language='en_US')
        text = text.lower()
        print('Your message:', format(text))

    except Exception as ex:
        print(ex)
        text = ""  # Define a default value for text

    if 'chrome' in text:
        a = 'Opening chrome...'
        engine.say(a)
        engine.runAndWait()
        program = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        subprocess.Popen([program])
    elif 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time', time)
        engine.say(time)
        engine.runAndWait()
    elif 'date' in text:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        print('Todays date', date)
        engine.say(date)
        engine.runAndWait()
    elif 'play' in text:
        b = 'Opening YouTube...'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    elif 'youtube' in text:
        b = 'Opening YouTube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    elif 'how are you' in text:
        response = 'I am fine, how about you'
        print(response)
        engine.say(response)
        engine.runAndWait()
    elif 'what is your name' in text:
        response = 'I am Siri, what can I do for you?'
        print(response)
        engine.say(response)
        engine.runAndWait()
    elif 'exit' in text:
        print("Exiting the program...")
        engine.say("Exiting the program...")
        engine.runAndWait()
        return False  # Return False to break the loop
    elif 'instagram' in text:
        c = 'Opening Instagram'
        engine.say(c)
        engine.runAndWait()
        webbrowser.open('www.instagram.com')
    elif 'linkedin' in text:
        d = 'Opening LinkedIn'
        engine.say(d)
        engine.runAndWait()
        webbrowser.open('www.linkedin.com')
    elif 'github' in text:
        e = 'Opening GitHub'
        engine.say(e)
        engine.runAndWait()
        webbrowser.open('www.github.com')
    elif 'facebook' in text:
        f = 'Opening Facebook'
        engine.say(f)
        engine.runAndWait()
        webbrowser.open('www.facebook.com')
        
    return True  # Return True to continue the loop

while True:
    if not cmd():
        break