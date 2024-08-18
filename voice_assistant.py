import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import sys
import psutil  # Import psutil to check battery status

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

# Define lambda functions for each command
open_chrome = lambda text: 'chrome' in text and (engine.say('Opening chrome..'), engine.runAndWait(), subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe"]))
tell_time = lambda text: 'time' in text and (lambda t: (print(t), engine.say(t), engine.runAndWait()))(datetime.datetime.now().strftime('%I:%M %p'))
tell_date = lambda text: 'date' in text and (lambda d: (print(d), engine.say(d), engine.runAndWait()))(datetime.datetime.now().strftime('%B %d, %Y'))
play_on_youtube = lambda text: 'play' in text and (engine.say('Opening YouTube..'), engine.runAndWait(), pywhatkit.playonyt(text))
open_youtube = lambda text: 'youtube' in text and (engine.say('Opening YouTube..'), engine.runAndWait(), webbrowser.open('www.youtube.com'))
exit_program = lambda text: 'exit' in text and (engine.say('Exiting program...'), engine.runAndWait(), sys.exit())
tell_name = lambda text: 'name' in text and (engine.say("My name is Rosie."), engine.runAndWait())
how_are_you = lambda text: 'how are you' in text and (engine.say("I'm just a program, but I'm here to help you!"), engine.runAndWait())
open_facebook = lambda text: 'facebook' in text and (engine.say('Opening Facebook..'), engine.runAndWait(), webbrowser.open('http://www.facebook.com'))
open_instagram = lambda text: 'instagram' in text and (engine.say('Opening Instagram..'), engine.runAndWait(), webbrowser.open('http://www.instagram.com'))
open_github = lambda text: 'github' in text and (engine.say('Opening GitHub..'), engine.runAndWait(), webbrowser.open('http://www.github.com'))
open_linkedin = lambda text: 'linkedin' in text and (engine.say('Opening LinkedIn..'), engine.runAndWait(), webbrowser.open('http://www.linkedin.com'))
check_battery = lambda text: 'battery' in text and (lambda b: (print(f"Battery percentage: {b}%"), engine.say(f"Battery percentage is {b} percent"), engine.runAndWait()))(psutil.sensors_battery().percent)


def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        recordedaudio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US').lower()
        print('Your message:', format(text))

        # Execute the appropriate command using the lambda functions
        open_chrome(text)
        tell_time(text)
        tell_date(text)
        play_on_youtube(text)
        open_youtube(text)
        exit_program(text)
        tell_name(text)
        how_are_you(text)
        open_facebook(text)
        open_instagram(text)
        open_github(text)
        open_linkedin(text)
        check_battery(text)

    except Exception as ex:
        print(ex)

while True:
    cmd()
