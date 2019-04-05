import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('wolfram id')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak (audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant LARVIS the Lady Jarvis!')
speak('How may I help you?')

def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language = 'en-us')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try saying the command again.')
        query = myCommand()


    return query

if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'youtube' in query:
            speak('opening YouTube')
            webbrowser.open('www.youtube.com')

        elif 'maps' in query:
            speak('opening Google Maps')
            webbrowser.open('www.googlemaps.com')

        elif 'google' in query:
            speak('opening Google')
            webbrowser.open('www.google.com')

        elif 'gmail' in query:
            speak('opening Gmail')
            webbrowser.open('www.gmail.com')

        elif 'yahoo' in query:
            speak('opening Yahoo')
            webbrowser.open('www.yahoo.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nince and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient?')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("your_username", 'your_password')
                    server.sendmail('fromaddr', "toaddr", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif "where is" in query:
           data = query.split("where is ")
           location = data[1]
           speak("Hold on your_name, I will show you where " + location + " is.")
           webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")
           
        else:
            query = query
            speak('Searching...')
            try:
                res = client.query(query)
                results = next(res.results).text
                speak('WOLFRAM-ALPHA says - ')
                speak('Got it.')
                speak(results)
  
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')
        speak('Next command! Sir!')

        
                    
