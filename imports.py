__author__ = 'Stephen Ford'
__version__ = 'v 0.1'

"""
- Control programs with your voice
"""

# import modules
from datetime import datetime  # datetime module supplies classes for manipulating dates and times

import \
    speech_recognition as sr  # speech_recognition Library for performing speech recognition with support for Google Speech Recognition, etc..

# pip install pyttsx3                   # need to run only once to install the library

# importing the pyttsx3 library
import pyttsx3
import webbrowser as wb

# initialisation
engine = pyttsx3.init()

chrome_path = '/usr/lib/firefox/firefox'
