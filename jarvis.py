import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui 
import pyjokes
import psutil
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning boss")
    elif hour>=12 and hour<18:
        speak("good afternon boss")
    else:
        speak("good night boss")

    speak("i am gru ,your personal assistant, tell me how may i help you")


    

def takeCommand():
  

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 




    except Exception as e:
        # print(e)    
        print("Say that again please...")   
       
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aryarajasa0@gmail.com','arduino27')
    server.sendmail('aryarajasa0@gmail.com', to, content)
    server.close()

def screenshot(): 
    image=pyautogui.screenshot()
    image.save('C:/Users/Yudhistira Arya/Pictures/Screenshots/ss.png')
    

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )

def jokes():
    speak(pyjokes.get_joke())




if __name__ == "__main__":
    wishMe()
    while True:
     
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'what is ' or 'who is' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Yudhistira Arya\\Music\\MEmu Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"boss, the time is {strTime}")
            
            
        elif 'chrome' in query:
            try: 
               speak("What should i search ?")
               chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
               search = takeCommand().lower()
               webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

               webbrowser.get('chrome').open(search + ".com")

            except Exception as e:
                print(e) 
                speak("Uable to search")
               
        elif 'logout' in query: 
            os.system("shutdown -l")
            
        elif 'shutdown' in query: 
            os.system("shutdown /s /t 1") 
            
        elif 'restart' in query: 
            os.system("shutdown /r /t 1")
            
        elif 'screenshot' in query: 
            screenshot() 
            speak("Done!") 
        
        
        elif 'cpu' in query: 
            cpu()
                
        elif 'jokes' in query: 
            jokes()
        
        elif 'offline' in query:
            quit()

        elif 'search' in query:
            speak("what i must search")
            search = takeCommand().lower()
            g_url="https://www.google.com/search?q="    
            res_g = 'this is what i found'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+search)     

      
        
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "personcase0@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my sirr. I am not able to send this email")
            
        
         
           
          