import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import pywhatkit
import datetime
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def design1():
        os.system(" cls ")
        os.system(" tput bold ")
        print()
        print("===============================================================================================================================================")
        os.system(" tput  setaf 1 ") 
        print("\t\t\t ----------------->Your welcome in this Basic Automation Menu Program<----------------\t\t")
        os.system(" tput  setaf 3 ")
        print("===============================================================================================================================================\n")
        os.system(" tput setaf 77 ")

def design2():
        os.system(" tput setaf 68 ")
        print(" Basic Menu Program ")
        print(" ----------------------\n")
        os.system(" tput setaf 78 ")      
        print(""" \t\t 1). Search Wikipedia \t\t 2). Open Youtube \t\t 3). Open Google Chrome \n
                 4). Open StackOverFlow \t 5). Play Music \t\t 6). Current Time \n
                 7). Tell me a Joke \t\t 8). Show Network Configuration  9). Open VS Code Editor \n
                10). Open PyCharm Editor \t 11). Open Oracle Virtual Box \t 12). Open Team Viewer\n
                13). Open Notepad Editor \t 14). Open Window Media Player \t 15). WhatsApp Message\n\n """)
                                   
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        os.system(" tput  setaf 1 ") 
        print(" I am listening....\n")
        speak(" Tell me your requirements......")
        r.pause_threshold = 1 
        audio = r.listen(source)
      
    try:
        print(' Recognising....\n')
        speak("I got it, please wait.....")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        print('Say that again please...\n')
        speak('Say that again please...')
        return 'None'

    return query

while True: 
        os.system(" cls ")
        design1()
        design2()
        query = takeCommand().lower()
  
        if 'wikipedia' in query:
            print('Searching on wikipedia....')
            query = query.replace('wikipedia', '') 
            results = wikipedia.summary(query, sentences = 1)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query or 'play youtube' in query:
            speak(" playing youtube " )
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak(" opening google ")
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            speak(" running stack overflow ")
            webbrowser.open('stackoverflow.com')

        elif 'play song' in query:
            song = query.replace(" play song ",  ' ' )
            speak(" Playing " + song )
            pywhatkit.playonyt(song)

        elif 'time' in query:
            time = datetime.datetime.now().strftime(" %I:%M %p ")
            print(time, "\n")
            speak(" Current time is " + time )

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke, "\n")
            speak(joke)

        elif 'whatsapp message' in query:
            speak(" Sending WhatsApp message ")
            pywhatkit.sendwhatmsg(' +919034145074 ',  ' Hello, How are you ? ' , 10, 27 ) 

        elif 'open vs code' in query:
            speak(" Opening VS Code ")
            vsCodePath = "C:\\Users\\sargam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsCodePath)

        elif 'open pycharm' in query:
            speak(" Opening Pycharm ")
            PyChm = "C:\\Program Files\\JetBrains\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe"
            os.startfile(PyChm)

        elif 'open oracle virtual box' in query:
            speak(" Opening Oracle Virtual Box ")
            oracleVB = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile(oracleVB)
        
        elif 'open teamviewer' in query:
            speak(" Opening Teamviewer ")
            tmViewer = "C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe"
            os.startfile(tmViewer)

        elif  (("run" in query) or  ("execute" in query) or ('open' in query ))  and ("chrome" in query):
            speak(" Opening Chrome ")
            os.system("chrome")

        elif  (("run" in query) or ("execute" in query) or ('open' in query)) and (("notepad" in query) or ("editor" in query)):
            speak(" Opening Notepad Editor ")
            os.system("notepad")

        elif  (("run" in query) or ("execute" in query) or ('open' in query)) and ("media" in query) and ("player" in query):
            speak(" Opening Media Player ")
            os.system("wmplayer")

        elif "network configuration" in query:
            speak(" Network Configurations are ")
            os.system("ipconfig")

        elif 'go to main menu' in query:
            os.system(" tput setaf 2 ")
            print("-------------------------------------")
            print('Thankyou sir for using my services :)')
            print("-------------------------------------\n")
            speak('Thankyou sir for using my services')
            break

        else:
            print(" Please say the command again....")
            speak(" Please say the command again")

        input(" Please enter to continue......\n")
        os.system(" tput setaf 99 ")