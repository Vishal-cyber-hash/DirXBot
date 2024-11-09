type:- ico
.\myenv\Scripts\activate  


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        speak("Opening "+query)
        os.system('start '+query)
    else:
        speak("Sorry sir, I don't understand what you are saying")



def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)


feture


import webbrowser
import playsound as playsound
import eel
import os 
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import re
import sqlite3
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

# Playing Assiantnt sound Functions
@eel.expose
def playAssistanSound():
    mudsic_dir ="www/assets/Audio/start_sound.mp3"
    playsound.playsound(mudsic_dir)



def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")



def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None







<!-- Command -->
Open app_name (Like open google)
Open  url (Like open youtube)
Play Song on youtube (Like open song on youtube)
<!-- Command -->

