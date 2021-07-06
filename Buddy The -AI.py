from ntpath import join
from sys import path
from urllib.request import urlcleanup
from bs4 import BeautifulSoup
from requests import get
from cv2 import data
from wikipedia import exceptions
import pyttsx3
import datetime
import speech_recognition as sr
import pywhatkit as kit
import os
import sys
import random
import cv2
import wikipedia
import webbrowser
import smtplib
import requests
import pyautogui
import wolframalpha
import time
import instaloader
import pyautogui
import pywikihow
import speedtest
import pyjokes
import json
from wikipedia.wikipedia import search

print("Initializing Buddy")

strTime = datetime.datetime.now().strftime("%H:%M:%S")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


#print(voices[2].id)
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 180)

#text to speech
def speak(audio):
   engine.say(audio)
   print(audio)
   engine.runAndWait()

#Tells time
def wishMe():
   hour = int(datetime.datetime.now().hour)
   tt = time.strftime("%I:%M %p")
  
   if hour>=0 and hour<12:
      speak(f"Good Morning, its {tt}")
      
   elif hour>=12 and hour<18:
      speak(f"Good Afternoon, its {tt}")
     
   else:
      speak(f"Good evening, its {tt}")
   speak("I am Buddy Sir. please tell me how can i help you")

#To covert speech to text
def takecommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("listening....")
      r.pause_threshold = 1
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source,timeout=5,phrase_time_limit=10)

   try:
      print("Recognizing....")
      query = r.recognize_google(audio, language='en-in')
      print(f"user said: {query}")

   except sr.WaitTimeoutError as k :
    print("time out")
   
   except Exception as e:
         #speak("Say that again sir....")
         return "none"
   query = query.lower()      
   return query

#sends email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rajenroy9999@gmail.com', 'rajenkumarroy99')
    server.sendmail('rajenroy9999@gmail.com', to, content)
    server.close()

def search_wikihow(query, max_results=10, lang='en'):
    return list(pywikihow.search_wikihow(query, max_results, lang))


app = wolframalpha.Client("788AWJ-QVRWVJ8Y42")



def TaskExecution():
   wishMe() 
   while True:
      query = takecommand().lower()
  
      #Logic building for tasks
      if "wikipedia" in query: 
           speak('searching wikipedia....')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)

      elif "open youtube" in query:
         speak("Sir what should i search on youtube")
         cm1 = takecommand().lower()
         result = "https://www.youtube.com/results?search_query=" + cm1
         webbrowser.open(result)   

      elif "open google" in query:
         speak("Sir what should i search on google")
         cm = takecommand().lower()
         result1 = "https://www.google.com/results?search_query=" + cm
         webbrowser.open(f"{result1}")

      elif "open facebook" in query:
         webbrowser.open("facebook.com")           

      elif "play music" in query:
         music_dir = r'D:\\music'
         song = random.choice(os.listdir(music_dir))
         speak(song)
         print('Song Name:', song)
         os.startfile(music_dir+'\\'+song)

      elif "stop music" in query:
         speak("ok sir stop music")
         os.system("taskkill /f /im wmplayer.exe")

      elif "my ip address" in query:
         ip = get('https://api.ipify.org').text
         speak(f"Your ip adress is {ip}")

      elif "the time" in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir The time is {strTime}")
      
      elif "open notepad" in query:
         npath = "C:\\WINDOWS\\system32\\notepad.exe"
         os.startfile(npath)

      elif "close notepad" in query:
         speak("ok sir.. closing Notepad")
         os.system("taskkill /f /im notepad.exe")

      elif "open firefox" in query:
         npath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
         os.startfile(npath)
  
      elif "close firefox" in query:
         speak("closing firefox")
         os.system("taskkill /f /im firefox.exe")

      elif "open command prompt" in query:
         os.system("start cmd")

      elif "send email to abhijeet" in query:
         try:
            speak("what should i say....")   
            content = takecommand().lower()
            to = "babin.kar100@gmail.com"
            speak("Okay sir, whats the subject for this mail")
            query = takecommand().lower()
            subject = query
            sendEmail(to, content)
            speak("Email has been sent sir....")
         except Exception as e:
            print(e)
            speak("sorry sir i am not able to send email")   

      elif "search" in query :
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
        
      elif "camera"  in query:
        cap = cv2.VideoCapture(0)
        while True:
           ret, img = cap.read()
           cv2.imshow('webcam', img)
           k = cv2.waitKey(50)
           if k==27:
               break;
        cap.release()
        cv2.destroyAllWindows()
 
      elif "youtube" in query:
           query = query.replace("search", "")
           query = query.replace("play", "")  
           kit.playonyt(query)
    #Tells Joke
      elif "tell me a joke" in query:
           joke = pyjokes.get_joke()
           speak(joke)
    #internet speed
      elif "internet speed" in query: 
         speak("Checking internet speed wait...")
         #os.system('cmd /k "speedtest"')
         speak("Calculating...")
         
         st = speedtest.Speedtest()
         dl = st.download()
         up = st.upload()
         speak(f"Sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

      elif "calculate" in query:
         speak("what should i calculate")
         gh = takecommand().lower()
         res = app.query(gh)
         speak(next(res.results).text)

      elif "change the window" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")

      elif "find temperature" in query:
         #speak("sir please tell me the city name")
         #search = takecommand().lower()
         search = "temperature in kolkkata"
         url = f"https://www.google.com/search?q={search}"
         r = requests.get(url)
         data = BeautifulSoup(r.text,"html.parser")
         temp = data.find("div",class_="BNeawe").text
         speak(f"current{search} is {temp}")

      elif "set alarm" in query:
         speak("setting alrm for 9 pm")
         nn = int(datetime.datetime.now().hour)
         if nn==21:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("alarm has been set")      
     #to check insta profile
      elif "instagram profile" in query or "profile on instagram" in query:
         speak("Sir please enter the username correctly!....")
         name2 = input("Enter the user name here:")
         webbrowser.open(f"instagram.com/{name2}")
         speak(f"sir here is the profile of the user {name2}") 
         time.sleep(5)
         speak("Sir would u like to download profile picture of this account.")
         condition = takecommand().lower()
         if "yes" in condition:
            mod = instaloader.instaloader()
            mod.download_profile(name2, profile_pic_only=True)
            speak("i am done sir, pprofile picture has been saved in our main directory")
         else:
            pass
     #take screenshot
      elif "take screenshot"  in query:
         speak("sir please tell me the name for the screenshot")
         name3 = takecommand().lower()
         speak("Please hold the screen for few seconds sir, i am taking screenshot")
         time.sleep(3)
         img = pyautogui.screenshot()
         img.save(f"{name3}.png")
         speak("I am done sir , the screenshot has been taken and saved in our main folder")
           
      elif "activate how to do mod" in query:
         speak("how to do mode is activated. Please tell me what you want to know")
         how = takecommand()
         max_results = 1
         how_to = search_wikihow(how, max_results)
         assert len(how_to) == 1
         how_to[0].print()
         speak(how_to[0].summary)

      elif "vaccine report" in query:
         speak("Opening Your certificate sir.")
         vaccine = "https://drive.google.com/file/d/1EjSDYXLNqnDR_ktlN-m9vaW3rw-8FFIz/view?usp=sharing"
         webbrowser.open(vaccine)

     #AI Talking
      elif "how are you" in query:
         speak("I am fine, Thank you....")
         speak("glad to hear that sir!....")
         speak("How are you, Sir....")    

      elif "hello" in query:
          speak("Hello sir! may i help u with something....")

      elif "fine" in query or "good" in query:
            speak("It's good to know that your fine.")

      elif "what is your name" in query:
            speak("My friend call me Buddy.")
            speak("I am Buddy 1 point o  created by Rajen Roy.")
         
      elif "i love you" in query:
            speak("Its hard to understand.")
            speak("padhai likhai karo IAS YAS bano aur desh ko sudhaaro")

      elif "thanks" or "thankyou" in query:
         speak("It's my pleasure sir" )

      elif "bye buddy" in query:
         speak("Bye sir!..Thakyou for using me, see you soon")
         break;        

      elif "developed you"  in query:
         speak("Rajen Roy have developed me as a minor project" )


if __name__ == '__main__':
    while True:
       permission = takecommand().lower()
       if "wake up" in permission or "time to wake up" in permission:
          speak("Buddy Intialized")
          TaskExecution()

       elif "shutdown" or "break" in permission:
            speak("bye sir")
            sys.exit()
        


