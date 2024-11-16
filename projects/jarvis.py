import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')  # for taking voice 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')  # Voice speed set
engine.setProperty('rate', 160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak("I am EDITH, Please tell me how may I help you..")

def takeCommand():
    # it takes microphone input from user and return output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: , {query}\n")
        
    except Exception as e:
        # print(e)
        
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('siddharthrai251@gmail.com', 'Anchalrai9616@gmail.com')
    server.sendmail('siddharthrai251@gmail.com',to, content )
    server.close()

if __name__ == "__main__":
    wishme()
    # while True:
    if 1:
        query = takeCommand().lower()
        
        # Logic for executing task based on query
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("Youtube.com")
            
        # elif 'open google' in query:
        #     speak("Opening Google")
        #     webbrowser.open("google.com")
            
        elif 'open stack overflow' in query:
            speak("Opening stack overflow")
            webbrowser.open("stackoverflow.com")
            
        elif 'open spotify' in query:
            speak("Opening Spotify")
            os.system("spotify")
            
        elif 'open whatsapp' in query:
            speak("Opening WhatsApp")
            os.system("start WhatsApp")
            
        elif 'open notepad' in query:
            speak("Opening notepad")
            os.system("notepad")
            
        elif 'open word' in query:
            speak("Opening word")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
            
        elif 'open instagram' in query:
            speak("opening instagram")
            os.system("Instagram")
            
            
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Siddharth Rai\\Music'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open vs code' in query:
            codepath= "C:\\Users\\Siddharth Rai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening vs code")
            os.startfile(codepath)    
            
        elif 'email to siddharth' in query:
            try:
                speak("What should I say")
                content= takeCommand()
                to= "raisid9616@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Siddharth. I am not able to send this email")
                
            
            
        