#!/usr/bin/python

import os
import sys
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import subprocess
from subprocess import call

__author__ = 'Stephen Ford'
__version__ = 'v 0.1'

# Initialization
engine = pyttsx3.init()

chrome_path = '/usr/lib/firefox/firefox'

# Obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    engine.say("Say something")
    engine.runAndWait()
    audio = r.listen(source)

# Recognize speech using Google Speech Recognition
Query = ''
try:
    Query = r.recognize_google(audio)

    if Query == "today's date":
        engine.say("Today's date is " + str(datetime.now().strftime("%d %B %Y")))
        engine.runAndWait()
    else:
        print("You said: " + Query)
        engine.runAndWait()

    if 'search for' in Query:
        search_query = Query[10:]
        engine.say("Searching for " + search_query)
        engine.runAndWait()
        search_url = 'https://www.google.com/search?q=' + search_query
        wb.get(chrome_path).open(search_url)

    if 'mute' in Query:
        mute_command = 'amixer sset Master mute'
        unmute_command = 'amixer sset Master unmute'

        def sys_message(msg):
            subprocess.call(['notify-send', '-t', '1000', '{}'.format(msg)])

        process = subprocess.Popen(['amixer sget Master'], shell=True, stdout=subprocess.PIPE)
        output = process.communicate()[0].decode()
        is_mute = False

        for line in output:
            data = line.lower()
            if ('front left' in data) and '[off]' in data:
                is_mute = True

        if is_mute:
            p = subprocess.Popen(['amixer sset Master unmute'], shell=True, stdout=subprocess.PIPE)
            sys_message("Mute was disabled")
        else:
            p = subprocess.Popen(['amixer sset Master mute'], shell=True, stdout=subprocess.PIPE)
            sys_message("Mute was enabled")

    if 'unmute' in Query:
        mute_command = 'amixer sset Master mute'
        unmute_command = 'amixer sset Master unmute'

        def sys_message(msg):
            subprocess.call(['notify-send', '-t', '1000', '{}'.format(msg)])

        process = subprocess.Popen(['amixer sget Master'], shell=True, stdout=subprocess.PIPE)
        output = process.communicate()[0].decode()
        is_mute = True

        for line in output:
            data = line.lower()
            if ('front left' in data) and '[off]' in data:
                is_mute = True

        if is_mute:
            p = subprocess.Popen(['amixer sset Master unmute'], shell=True, stdout=subprocess.PIPE)
            sys_message("Mute was disabled")
        else:
            p = subprocess.Popen(['amixer sset Master mute'], shell=True, stdout=subprocess.PIPE)
            sys_message("Mute was enabled")

        valid = False

        while not valid:
            volume = '70'

            try:
                volume = int(volume)

                if (volume <= 100) and (volume >= 0):
                    call(["amixer", "-D", "pulse", "sset", "Master", str(volume) + "%"])
                    valid = True

            except ValueError:
                pass

    if 'set volume' in Query:
        valid = False

        while not valid:
            engine.say('Set volume to?')
            engine.runAndWait()
            volume_audio = r.listen(source)

            try:
                volume = int(r.recognize_google(volume_audio))

                if 0 <= volume <= 100:
                    call(["amixer", "-D", "pulse", "sset", "Master", str(volume) + "%"])
                    valid = True
                else:
                    engine.say('Please provide a number between 0 and 100.')
                    engine.runAndWait()

            except ValueError:
                engine.say('Please say a valid number.')
                engine.runAndWait()

except sr.UnknownValueError:
    print("I could not understand audio")

except sr.RequestError as e:
    print("Error: {0}".format(e))

except Exception as e:
    print(e)

# Run application based on voice command
def get_app(query):
    if query == "time":
        print(datetime.now())
    elif query == '':
        engine.say("Sorry, please try again.")
        engine.runAndWait()

# Call get_app(Query) function
get_app(Query)
os.execv(sys.executable, [sys.executable] + sys.argv)
