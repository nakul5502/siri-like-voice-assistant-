import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import time

# ---------- Text To Speech ----------
engine = pyttsx3.init("nsss")
engine.setProperty("rate", 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ---------- Speech Recognition ----------
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language="en-in").lower()
    except:
        return ""

# ---------- Media Control (macOS) ----------
def play_pause():
    os.system(
        "osascript -e 'tell application \"System Events\" to key code 16'"
    )

def next_track():
    os.system(
        "osascript -e 'tell application \"System Events\" to key code 17'"
    )

def previous_track():
    os.system(
        "osascript -e 'tell application \"System Events\" to key code 18'"
    )

# ---------- Greeting ----------
def wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your assistant. Say hello to start.")

wish()

# ---------- Main Loop ----------
while True:
    command = take_command()

    if command == "":
        continue

    # Wake word
    if "hello" in command or "hey assistant" in command:
        speak("Yes, I am listening")

        while True:
            query = take_command()

            if query == "":
                continue

            # Time
            if "time" in query:
                speak("The time is " + datetime.datetime.now().strftime("%H:%M"))

            # Chrome
            elif "open chrome" in query:
                speak("Opening Google Chrome")
                os.system("open -a 'Google Chrome'")

            # YouTube video search
            elif "youtube video" in query or "play video" in query:
                speak("Which video should I play?")
                search = take_command()

                if search != "":
                    speak("Playing " + search)
                    webbrowser.open(
                        "https://www.youtube.com/results?search_query=" +
                        search.replace(" ", "+")
                    )
                    time.sleep(5)
                    speak("Please click the video to start")
                else:
                    speak("I did not hear the video name")

            # YouTube channel search
            elif "youtube channel" in query:
                speak("Which channel should I search?")
                channel = take_command()

                if channel != "":
                    speak("Searching YouTube channel " + channel)
                    webbrowser.open(
                        "https://www.youtube.com/results?search_query=" +
                        channel.replace(" ", "+") + "&sp=EgIQAg%253D%253D"
                    )
                else:
                    speak("I did not hear the channel name")

            # Media controls
            elif "pause video" in query or "stop video" in query:
                speak("Pausing the video")
                play_pause()

            elif "resume video" in query or "play video" in query:
                speak("Resuming the video")
                play_pause()

            elif "next video" in query:
                speak("Playing next video")
                next_track()

            elif "previous video" in query:
                speak("Playing previous video")
                previous_track()

            # WhatsApp
            elif "open whatsapp" in query:
                speak("Opening WhatsApp")
                webbrowser.open("https://web.whatsapp.com")

            # Camera
            elif "open camera" in query:
                speak("Opening camera")
                os.system("open -a Photo\\ Booth")

            # Terminal
            elif "open terminal" in query:
                speak("Opening terminal")
                os.system("open -a Terminal")

            # Sleep
            elif "sleep" in query:
                speak("Going to sleep")
                break

            # Exit
            elif "exit" in query or "quit assistant" in query:
                speak("Goodbye")
                exit()
