import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio= recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Not Understand")
            
def speechtx(x):
    engion= pyttsx3.init()
    voices= engion.getProperty('voices')
    engion.setProperty('voice', voices[1].id)# Through pass index 0 and 1 voice change
    rate= engion.getProperty('rate')  #Voice speed set
    engion.setProperty('rate', 130)
    engion.say(x)
    engion.runAndWait()
    
if __name__ == '__main__':
    
    
    # if sptext() == "hey peter":
        data1=sptext()
        if "your name" in data1:
            name= "my name is peter"
            speechtx(name)
        
    # else:
    #     print("Thanks")
    
            
    
                                               
