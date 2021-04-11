# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:09:24 2021

@author: Akv_04
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit as what
import datetime 
import smtplib
from time import sleep
Master='Aman Verma'


listener =sr.Recognizer()
py=pyttsx3.init()
voices=py.getProperty('voices')
py.setProperty('voice', voices[1].id)


def talk(text):
    py.say(text)
    py.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        talk("good morning" + Master)

    elif hour>=12 and hour<18:
        talk("good afternoon" + Master)

    else:
        talk("good Evening" + Master)

    talk(" Hello I am Hannah your assistant.")
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amanverma986@gmail.com', 'Password')
    server.sendmail("amanverma986@gmail.com", to, content)
    server.close()
    
def take_command():    
    try:
        with sr.Microphone() as source: 
            talk('Listening')
            print('Listening.......')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
    except:
         pass
    return command
def run():
    command=take_command()
    
    if 'hello' or 'hi' in command:
        talk(command+Master)
    
        
    if 'play' in command:
        talk('playing' + command.lstrip('play'))
        print('playing' + command.lstrip('play'))
        what.playonyt(command)
        sleep(10)
            
    
   
    if 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M:%S')
        talk('Current Time is'+time)
        print(time)
        
   
    if 'send email' in command:
        try:
            
            talk('what should i send')
            content = take_command()
            to = "amanverma986@gmail.com"
            sendEmail(to, content)
            talk('Email has been sent')
        except Exception as e:
            print(e)

   
def main():
    wishme()
    run()
    talk('How can i help you?')
    run()
    talk('Is there anything i can do for you')
    input1=take_command()
    while 'yes' in input1:
        run()
        talk('Is there anything i can do for you')
        input1=take_command()
        if 'nothing' or 'bye' in input1:
            talk('Good bye'+Master+' Have a good Day')
            break
            
if __name__=="__main__":
    main()    
        