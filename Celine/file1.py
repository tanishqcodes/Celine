# Once in your lifetime you should undergo great misery, may it be loss of a loved one, a heartbreak,
# anything. It's gonna bring out the best of you, a part of you; you'd have never seen
# and would teach you the art of self-love! :)
#LoveYourself:)

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from meaning_scrap import *
from sarcastic_jokes import *
from facts import *
from selenium import webdriver
from time import sleep
from pytube import YouTube

def speak(text):
    tts=gTTS(text=text,lang="en-us")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""
        try:
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: "+str(e))
    return said

text=get_audio().lower()

while(text!="bye"):

    if "hello" in text or "hi" in text or "hey" in text:
        speak("Hi! How are you")

    elif "facts" in text or "fact" in text:
        speak(tell_facts())

    elif "music" in text or 'song' in text or 'songs' in text:
        speak("Which song would you like me to play?")
        song_name=get_audio().lower()
        # song_name.lower()
        driver=webdriver.Chrome()
        driver.get(f"https://www.youtube.com/results?search_query={song_name}")
        driver.implicitly_wait(10)
        driver.find_element_by_id("video-title").click()
        print('Now ready to take new input!')
        text=get_audio().lower()
        continue

    elif "i am" in text or "fine" in text or "great" in text:
        speak("Great! What can I do for you? I can play music, tell facts, tell you meaning of words, open your social media networks and even download songs from youtube! So what would you like me to do?")


    elif "download" in text:
        speak("Which song would you like me to download?")
        to_download=text.split('download ')[1]
        driver=webdriver.Chrome()
        driver.get(f"https://www.youtube.com/results?search_query={to_download}")
        driver.implicitly_wait(10)
        driver.find_element_by_id("video-title").click()
        sleep(3)
        get_url=driver.current_url
        sleep(1)
        yt=YouTube(get_url)
        stream=yt.streams(only_audio=True)
        stream[0].download()
        print("Download Completed!:)")
    
    elif "instagram" in text:
        speak("Opening Instagram and logging into your account")
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://www.instagram.com')
        sleep(2)
        username="__iwritesometimes__"
        password="Tsp@223533"

        # Login to the instagram page 
        driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(username)


        driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(password)

        driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
        driver.implicitly_wait(10)

        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
        driver.implicitly_wait(10)

        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        driver.implicitly_wait(10)
        print("Waiting for your next commmand sir:)")


    elif "meaning of " in text:
        print(text)
        speak(find_meaning(text.split('of ')[1]))

    elif "your name" in text:
        speak("My name is Celine! ")

    elif "thank you" in text:
        speak("Glad I'm of help!")

    elif "means" in text or "meaning" in text:
        # text="meaning of freewill"
        # print('Scrapping meaning  from the web!')
        print(find_meaning(text.split('of ')[1]))
        # speak(find_meaning(text.split('of ')[1]))

    elif "jokes" in text or "sarcastic" in text or "joke" in text or "funny" in text or 'laugh' in text:
        speak(say_jokes())

    elif "bye" in text:
        speak("Bye Tanishq! Let me know when you need any help.")
        break

    text=get_audio().lower()