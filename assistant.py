import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

speak("Hello, how can I help you?")

while True:
    command = input("Enter command: ").lower()

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("Current time is " + time)

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "your name" in command:
        speak("My name is Tanushree Patratime"
              "")

    elif "who are you" in command:
        speak("I am your Python assistant")

    elif "exit" in command:
        speak("Goodbye")
        break

    else:
        speak("Sorry, I didn't understand")