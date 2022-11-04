import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os 
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir .Please tell me how may I help you")

# It take microphone input from the user and returnd sring output 
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo
#     server.starttls()
#     server.login('youremail@gmail.com','you-password')
#     server.sendmail('yourgamil@com',to,content)
#     server.close()

    
if __name__ == "__main__":
    wishMe()
    while True:
       query = takeCommand().lower()

       if 'wikipedia' in query:
         speak("Searching Wikipedia....")
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query,sentences=2)
    
         speak("According to wikipedia")
         print(results)
         speak(results)
       elif 'open youtube' in query:
           webbrowser.open('youtube.com')

       elif 'open google' in query:
           webbrowser.open('google.com')

       elif 'open stackoverflow' in query:
           webbrowser.open('stackoverflow.com')

       elif 'play music' in query:
           music_dir = "C:\\Users\\Bharati\\Videos\\musicdir"
           songs = os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))

       elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir ,the time is {strTime}")

       elif 'open code' in query:
          codePath = "C:\\Users\\Bharati\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codePath)

    #    elif 'email to bharti' in query:
    #        try:
    #           speak("what should i say?")
    #           content = takeCommand()
    #           to = "youremail@gmail.com"
    #           sendEmail(to,content)
    #           speak("email has been sent!")
    #         except Exception as e :
    #           print(e)
    #           speak("sorry Bharti I am not able to send this email")

       


# Logic for excuting task