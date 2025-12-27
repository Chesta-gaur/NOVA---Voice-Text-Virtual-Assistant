# import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary
import datetime

# recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 180)
    engine.setProperty("volume", 1.0)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)

qa = {
    ("who are you", "what are you", "tell me about you"): 
        "I am Nova, your virtual assistant. I can help you with browsing, music, search, time, and basic conversations.",

    ("who made you", "who created you", "who developed you"): 
        "I was developed as a Python-based virtual assistant project.",

    ("what can you do", "what are your features", "how can you help me"): 
        "I can open websites, play music, tell time, search the web, and respond to basic questions."
}

# def reply(text):
#     return text

def smart_reply(c):
    # generic conversational responses
    if "how are you" in c:
        return "I am doing great. How can I help you today?"
    
    elif "thank you" in c or "thanks" in c:
        return "You're welcome! Happy to help."
    
    elif "hello" in c or "hi" in c:
        return "Hello! How can I assist you?"

    elif "help" in c:
        return "You can ask me to open websites, play music, tell time, search the web, or ask about me."

    else:
        return "That sounds interesting. Could you please rephrase or ask something else?"

def processCommand(c):
    c= c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        return "Opening Facebook"

    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
        return "Opening Instagram"

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
        return "Opening Linkedin"

    elif "open whatsapp" in c:
        webbrowser.open("https://whatsapp.com")
        return "Opening Whatsapp"

    elif c.startswith("play"):
        song = c.replace("play ", "").strip()

        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
            return f"Playing {song}"
        
        else:
            return "Sorry, I could not find that song"

    elif "time" in c:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {time_now}"

    elif "date" in c:
        date_now = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today is {date_now}"

    elif "search" in c:
        query = c.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching for {query}"

    elif "exit" in c or "stop" in c:
        return "EXIT"

    else:
        for questions, answer in qa.items():
            for q in questions:
                if q in c:
                    return answer

        return smart_reply(c)
    
    return "Okay"



# Logic file should NEVER run loops when used with GUI.

# if __name__ == "__main__":
#     speak("Initializing Nova...")

#     # with sr.Microphone() as source:
#     #     recognizer.adjust_for_ambient_noise(source, duration=1)

#     while True:
#         try:
#             with sr.Microphone() as source:
#                 print("Recognizing voice...")
#                 # timeout=5 → waits max 5 seconds for speech, phrase_time_limit=5 → listens max 5 seconds
#                 audio = recognizer.listen(source,timeout=5, phrase_time_limit=5)
                
#             word = recognizer.recognize_google(audio)

#             if "nova" in word.lower():
#                 speak("Yes! How can I help you?")

#                 # Listen for command
#                 with sr.Microphone() as source:
#                     print("Listening for the command...")
#                     audio = recognizer.listen(source,timeout=5, phrase_time_limit=5)

#                 command = recognizer.recognize_google(audio)
#                 print("Command:", command)
#                 processCommand(command)

#         except sr.RequestError as e:
#             print(f"API error: {e}")
#         except Exception as e:
#             print(f"Unexpected error: {e}")