import PyPDF2
import psutil
import pyttsx3
import pywhatkit
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import datetime
import random
import pyjokes
from PyDictionary import PyDictionary
from playsound import playsound
from pytube import YouTube
import randfacts
import time
import pyautogui
import wolframalpha
import requests
import instaloader

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')  # getting details of the current voice
engine.setProperty('voice', voices[1].id)  # 1 for girl voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak("Welcome!! Hello I am Angel, Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 0.2)
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


if __name__ == "__main__":
    wishMe()
    takeCommand()
    while True:
        query = takeCommand().lower()  # Converting user query into lower case

        if 'hello' in query:
            speak("hi what can i help you")
            print("hi what can i help you")
        elif 'what is your name' in query:
            speak("My name is Angel, what is your good name")
            print("my name is Angel, what is your good name")
        elif 'my name is' in query:
            speak("nice to meet you,how can i help you")
            print("nice to meet you,how can i help you")
        elif 'are you a girl' in query:
            speak("I am not a girl I am your voice assistant")
        elif 'how are you' in query:
            speak('I am good how about you')
        elif 'Ok' in query:
            speak('How can I help you')
            print('How can I help you')
        elif 'i am also' in query:
            speak('nice to hear that')
        elif 'i feel' in query:
            speak('what can I do for you to change your mood')
            print('what can I do for you to change your mood')
        elif 'play any random music' in query:
            n = random.randint(0, 5)
            print(n)
            music_dir = 'F:\Music'
            songs = os.listdir(music_dir)
            print(songs[n])
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'volume up' in query:
            pyautogui.press('volumeup')
        elif 'volume down' in query:
            pyautogui.press('volumedown')
        elif 'mute' in query:
            pyautogui.press('volumemute')

        elif 'tell me a joke' in query:
            my_joke = pyjokes.get_joke(language="en")
            print(my_joke)
            speak(my_joke)
            playsound('F:\Music\Laugh.mp3')

        elif 'open google' in query:
            speak("Okay , opening google")
            webbrowser.open("https://www.google.com/search?q=")
        elif 'open youtube' in query:
            speak("Okay , opening youtube")
            webbrowser.open("https://www.youtube.com/")
        elif 'the time' in query:
            speak("please wait, let me check first")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        elif 'give me information of' in query:
            s3 = query.replace('give me information of', '')
            speak('here is what I found about' + s3)
            webbrowser.open('https://en.wikipedia.org/wiki/' + s3)
            speak('According to Wikipedia here is information of' + s3)

        elif 'find location of' in query:
            s4 = query.replace('find location of', '')
            speak('opening the map of' + s4)
            webbrowser.open('https://www.google.com/maps/place/' + s4)

        elif 'give me latest news of ' in query:
            s5 = query.replace('give me latest news of', '')
            speak('here is what I found about' + s5)
            webbrowser.open('https://timesofindia.indiatimes.com/topic/' + s5)

        elif 'fact' in query:
            fa = randfacts.get_fact()
            print(fa)
            speak('Did you know that' + fa)
            # playsound('F:\\Music\\wow.mp3')

        elif 'open gmail' in query:
            speak('opening the gmail')
            webbrowser.open('www.gmail.com')

        elif 'question' in query:
            speak('ask me...')
            print('ask me...')
            gh = takeCommand().lower()
            app = wolframalpha.Client("R8PWLA-RQEK4RQVRE")
            res = app.query(gh)
            print(next(res.results).text)
            speak(next(res.results).text)

        elif 'temperature' in query:
            speak('wait, let me check first')
            app1 = wolframalpha.Client("R8PWLA-RQEK4RQVRE")
            res1 = app1.query(query)
            print(next(res1.results).text)
            speak(next(res1.results).text)

        elif 'gallery' in query:
            speak('opening the photo gallery')
            path = "F:\gallery"
            os.startfile(path)

        elif 'download' in query:
            speak('ok please paste or type the link here first')
            url = input('past the link here=')
            vid = YouTube(url)
            speak('download is in process')
            vid.streams.first().download("F:\\download video from python")
            speak('downloading finish ')
            path1 = "F:\\download video from python"
            os.startfile(path1)

        elif 'save one instagram profile' in query:
            speak('Yes,please enter the user name correctly')
            name = input('Enter username here=')
            webbrowser.open(f"https://www.instagram.com/{name}")
            time.sleep(5)
            speak('would you like to download profile file of this account')
            gh1 = takeCommand().lower()
            if 'yes' in gh1:
                mod = instaloader.Instaloader()
                speak("downloading is in process")
                mod.download_profile(name, profile_pic_only=True)
                speak('I am done,profile picture is saved in our main folder now i am ready for next work')
            if 'no' in gh1:
                speak('ok what should i do for you now')


        elif 'take screenshot' in query:
            speak(' tell me name for this screenshot')
            name = input("Enter name here=")
            speak('Do you want to move to take screenshot of another screen')
            gh3 = takeCommand().lower()
            def screenshot():
                img = pyautogui.screenshot()
                img.save(f'F:\screenshots\\{name}.png')
                speak("I am done, screenshot is saved in screenshots folder, now i am ready for next work")
                print("I am done, screenshot is saved in screenshots folder, now i am ready for next work")
                path2 = "F:\screenshots"
                os.startfile(path2)
            if 'yes' in gh3:
                speak('ok change your screen to take screenshot i will wait')
                time.sleep(5)
                screenshot()
            if 'no' in gh3:
                speak('please hold the screen, i am taking the screenshot')
                print('please hold the screen, i am taking the screenshot')
                time.sleep(3)
                screenshot()

        elif 'alarm' in query:
            speak("enter the time ")
            time = input("Enter the time=")
            while True:
                time_ac = datetime.datetime.now()
                now = time_ac.strftime("%H:%M:%S")
                if now == time:
                    speak("Time to wake up")
                    playsound("Alarm.mp3")
                    speak('Alarm closed')
                elif now > time:
                    break

        elif 'ip address' in query:
            speak("wait, let me check first")
            ipAdd = requests.get('https://api.ipify.org').text
            print(ipAdd)
            speak(f'Ip address of your pc is {ipAdd}')

        elif 'read pdf' in query:
            speak('ok,let me open the pdf')
            path2 = 'F:\pdf.pdf'
            os.startfile(path2)
            book = open('F:\pdf.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            #time.sleep(4)
            print(f'total number of pages in this pdf are {pages}')
            speak(f'total number of pages in this pdf are {pages}')
            speak('please give me the page number i have to read')
            pg = int(input('please enter page number : '))
            page = pdfReader.getPage(pg)
            text = page.extractText()
            print(text)
            speak(text)

        elif 'meaning' in query:
            dictionary = PyDictionary()
            speak('which word you want meaning')
            print('which word you want meaning')
            word = takeCommand().lower()
            speak('please wait let me check')
            meaning = dictionary.meaning(word)
            print(f'meaning of {word} is')
            speak(f'meaning of {word} is')
            print(meaning)
            speak(meaning)

        elif 'battery' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f'your system have {percentage} percent battery')

        elif 'search' in query:
            s1 = query.replace('search', '')
            speak('searching' + s1)
            pywhatkit.search(s1)
        elif 'play' in query:
            s2 = query.replace('play', '')
            speak('playing' + s2)
            pywhatkit.playonyt(s2)

        elif "switch the window" in query:
            speak("Okay, Switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            os.system('shutdown /r')

        elif "close" in query:
            speak("Okay , closing tab of chrome")
            os.system("taskkill /f /im chrome.exe")

        elif 'thank you' in query:
            print('I am happy to help you')
            speak('I am happy to help you')

        elif "goodbye" in query:
            print('Alright, going offline. It was nice working with you')
            speak('Alright, going offline. It was nice working with you')
            exit()
