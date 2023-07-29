import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def jokes():
    joke1 = pyjokes.get_joke(language="en", category="all")
    print(joke1)
    speak(joke1)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def GreetMe():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        speak("good morning!")
    elif time > 12 and time < 16:
        speak("good after noon!")
    else:
        speak("good evening!")
    speak("my name is lenovo how may I help you")


def TakeCommand():
    # it takes microphone input from the user and return string input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    GreetMe()
    while True:
        query = TakeCommand().lower()

        if " in wikipedia" in query:
            speak("searching your query")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open spotify" in query:
            speak("opening spotify music ")
            webbrowser.open("spotify.com")
        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif "tell me a joke" in query:
            jokes()

        elif "open code" in query:
            codePath = "C:\\Users\\Vashu Tewari\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening visual studio code")
            os.startfile(codePath)
        elif "open facebook" in query:
            speak("opening facebook")
            webbrowser.open("facebook.com",new=[0])
        elif "open instagram" in query:
            speak("opening your instagram")
            webbrowser.open("instagram.com")
        elif "linkedin" in query:
            speak("opening  linked in") 
            webbrowser.open("linkedin.in")  
       
        
        
