import datetime
from email.message import EmailMessage
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import subprocess
import time
import json
import requests
import pywhatkit
import pyjokes



motivation_lst=["Any fool can write code that a computer can understand","First, solve the problem","Experience is the name everyone gives to their mistakes","In order to be irreplaceable, one must always be different","Java is to JavaScript what car is to Carpet","Knowledge is power"]

youngster=["i am youngster your personal assistant developed and built by Saksham Jain and you can tell me to do your various tasks and i acn help you to do them although i have not been built perfectly but there are some tasks i can help you with "]

email_list = {
    'friend': 'hritikagarwal316@gmail.com',
    'pink': 'jennie@blackpink.com',
    'lisa': 'lisa@blackpink.com',
    'irene': 'irene@redvelvet.com'
}


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
r=sr.Recognizer()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am youngster sir Please tell me how may i help you!!")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en=in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again Please!")
        speak("say that again please")
        return "None"
    return query
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('your email id', 'Password')
    email = EmailMessage()
    email['From'] = 'your email id'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

def computer_sleep(seconds_until_sleep=5, verbose=1):
    print("this pc was in sleep mode")

if __name__ == '__main__':
    wishMe()

    while True:

        query=takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google enjoy safe surfing sir")

        elif 'open stack overflow' in query:
            webbrowser.open("https://dev.stackoverflow.com/users/login?ssrc=head")
            speak("opening stackover flow sir best whishes you find your solution here")

        elif 'play' in query:
            command=takeCommand()
            song=command.replace("play","")
            pywhatkit.playonyt(song)
            speak("playing"+song)

        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime('%Hhours:%Mminutes:%Seconds')
            speak(f"sir the time is{strtime}")

        elif 'open python' in query:
            speak("opening sir")
            for word in motivation_lst:


                pycharmpath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"
                os.startfile(pycharmpath)

            r=random.choice(motivation_lst)
            speak(r)



        elif 'send mail' in query:

            try:
                speak('To Whom you want to send email')
                name = takeCommand()
                receiver = email_list[name]
                print(receiver)
                speak('What is the subject of your email?')
                subject = takeCommand()
                speak('Tell me the text in your email')
                message = takeCommand()
                send_email(receiver, subject, message)
                speak('Your email is sent')
            except Exception  as e:
                print(e)
                speak("so sorry sir unable to send the email at this moment")

        elif 'open facebook' in query:
            webbrowser.open("https:///www.facebook.com//login.php")
            speak("opening facebook please login to your account sir")

        elif 'open instagram' in query:
            webbrowser.open("https:///www.instagram.com//accounts//login//")
            speak("opening instagram please login to your account sir")

        elif 'open calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            speak("opening calculator")

        elif 'open Notepad' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            speak("opening notepad")

        elif "set a reminder" in query:
            speak('what should i remind you sir')
            print("please speak")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                audio_text = r.listen(source)
                print("please speak i am listening")
                speak("in how many minutes please enter")
                tym=int(input("in how many minutes please enter"))
                tym1=tym*60
                time.sleep(tym1)
                print(audio_text)
                speak("excuse me sir you have remind me of telling you")
                speak("do you want to continue help me sir")
                if "yes" in query:
                    continue
                elif "no" in query:
                    break

        elif "tell me a joke" in query:
            speak("listen carefully")
            speak(pyjokes.get_joke())


        elif  "who are you" in query:

            speak(youngster)



        elif "news" in query:
            speak("News For Today....let's begin")
            url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=41e578ed35ce478aaf72c4cf7a9d1763"
            news=requests.get(url).text
            news_dict=json.loads(news)
            print(news_dict["articles"])
            arts= news_dict['articles']
            for article in arts:
                speak(article['title'])
                speak("moving on the next news")
            speak("Thanks for you time u were a great listener")

        elif "sleep" in query:
            speak("sleep mode on")
            computer_sleep()

        elif "search" in query:
            command=takeCommand()
            result=command.replace("search","")
            pywhatkit.search(result)
            speak("searching"+result)

        elif "hello" in query:
            command=takeCommand()
            handWritten=command.replace("write","")
            pywhatkit.text_to_handwriting(handWritten,rgb=[0,0,0])
            speak("writing"+handWritten)
        elif "stop" in query:
            break







