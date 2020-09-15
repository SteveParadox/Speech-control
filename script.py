
#!/usr/bin/python


import os
import sys

__author__ = 'Stephen Ford'
__version__ = 'v 0.1'

"""
- Control programs with your voice
"""

# import modules
from datetime import datetime  # datetime module supplies classes for manipulating dates and times

import \
    speech_recognition as sr  # speech_recognition Library for performing speech recognition with support for Google
# Speech Recognition, etc..

# pip install pyttsx3                   # need to run only once to install the library

# importing the pyttsx3 library
import pyttsx3
import webbrowser as wb
import subprocess
from subprocess import call



# initialisation
engine = pyttsx3.init()

chrome_path = '/usr/lib/firefox/firefox'

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    # engine.say("Say something")
    engine.runAndWait()
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
Query = ''
try:
    Query = r.recognize_google(audio)

    # print("I thinks you said '" + str(r.recognize_google(audio)) + "'")
    with sr.Microphone() as source:
        if Query == "today's date":
            engine.say("Today's date is '" + str(datetime.now().strftime("%d%B%Y")) + "'")
            engine.runAndWait()
        else:
            # engine.say("I thinks you said '" + str(r.recognize_google(audio)) + "'")
            print("I thinks you said '" + str(r.recognize_google(audio)) + "'")
            engine.runAndWait()

        if 'search for' in Query:
            engine.say("Searching for '" + (str(r.recognize_google(audio))[10:]) + "'")
            print((str(r.recognize_google(audio))[10:]))
            engine.runAndWait()
            f_text = 'https://www.google.co.in/search?q=' + Query[10:]
            print(f_text)
            wb.get(chrome_path).open(f_text)
        if 'mute' in Query:
            mute_command = 'amixer sset Master mute'
            unmute_command = 'amixer sset Master unmute'


            def sys_message(msg):
                subprocess.call(['notify-send', '-t', '1000', '{}'.format(msg)])


            process = subprocess.Popen(['amixer sget Master'], shell=True, stdout=subprocess.PIPE)
            output = f'b{process.communicate()[0]}'
            is_mute = False

            for line in output:
                data = line.lower()
                if ('front left' in data) and '[off]' in data:
                    is_mute = True
            if is_mute:
                p = subprocess.Popen(['amixer sset Master unmute'], shell=True, stdout=subprocess.PIPE)
                sys_message("Mute foi desativado")  # mute was disabled6
            else:
                p = subprocess.Popen(['amixer sset Master mute'], shell=True, stdout=subprocess.PIPE)
                sys_message("Mute foi ativado")  # mute was enabled
        if 'unmute' in Query:
            mute_command = 'amixer sset Master mute'
            unmute_command = 'amixer sset Master unmute'


            def sys_message(msg):
                subprocess.call(['notify-send', '-t', '1000', '{}'.format(msg)])


            process = subprocess.Popen(['amixer sget Master'], shell=True, stdout=subprocess.PIPE)
            output = f'b{process.communicate()[0]}'
            is_mute = True

            for line in output:
                data = line.lower()
                if ('front left' in data) and '[off]' in data:
                    is_mute = True
            if is_mute:
                p = subprocess.Popen(['amixer sset Master unmute'], shell=True, stdout=subprocess.PIPE)
                sys_message("Mute foi desativado")  # mute was disabled
            else:
                p = subprocess.Popen(['amixer sset Master mute'], shell=True, stdout=subprocess.PIPE)
                sys_message("Mute foi ativado")  # mute was enabled

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
                engine.say('set volume to?')
                volume = r.recognize_google(audio)
                engine.runAndWait()


                try:
                    volume = int(volume)

                    if (volume <= 100) and (volume >= 0):
                        call(["amixer", "-D", "pulse", "sset", "Master", str(volume) + "%"])
                        valid = True

                except ValueError:
                    engine.say('say a number asshole')
                    engine.runAndWait()

# except sr.UnknownValueError:
#  print("I could not understand audio")
except sr.RequestError as e:
    print("error; {0}".format(e))

except Exception as e:
    print(e)


# Run Application with Voice Command Function
def get_app(Q):
    if Q == "time":
        print(datetime.now())

    elif Q == '':
        # engine.say("Sorry Try Again")
        engine.runAndWait()

    return


# Call get_app(Query) Func.
get_app(Query)
os.execv(sys.executable, [sys.executable] + sys.argv)


