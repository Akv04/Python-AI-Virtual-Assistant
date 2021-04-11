# Python-AI-Virtual-Assistant

Speech_recognition

Library for performing speech recognition, with support for several engines and APIs, online and offline.

Installation:
pip install SpeechRecognition

Usage:

import speech_recognition as sr
listener =sr.Recognizer()
voices=py.getProperty('voices')        # to get the list of voices available
py.setProperty('voice', voices[1].id)  # change voice to female voice ( voice[1]) . You can use voice[0] for male voice).
Recognize speech input from the microphone

pyttsx3
pyttsx3 is a t
ext-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3

Installation:

pip install pyttsx3

If you recieve errors such as No module named win32com.client, No module named win32, or No module named win32api, you will need to additionally install pypiwin32.

Usage :

import pyttsx3
py=pyttsx3.init()
py.say('Hello Everyone This will Speak')
py.runAndWait()


Pywhatkit

PyWhatKit is a Python library for Sending whatsapp message at certain time, it has several other features too. I have used this to play music on youtube.

Installation:

pip install pywhatkit

Usage:

Import the library using the following command.

import pywhatkit

what.playonyt('Play Brown Munde')                   # It Will play Brown Munde on Youtube


import smtplib

It is used to send emails using SMTP(Simple Mail Transfer Protocol


from time import sleep

It is used to add time delay.




