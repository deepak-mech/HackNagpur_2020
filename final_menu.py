import os
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def design1():
	os.system(" cls ")
	os.system(" tput bold ")
	print(" \t\t\t\t**********************************************************************************************")
	os.system(" tput  setaf 1 ")
	print(" \t\t\t\t\t\t!!------->> Welcome to this Automation World <<--------!!\t\t ")
	os.system(" tput  setaf 2 ")
	print(" \t\t\t\t**********************************************************************************************\n")

def design2():
	print("--------------------------------------------------------")
	os.system(" tput setaf 25 ")
	print("\tLocal Host --------> Window")
	print("\tRemote Host --------> AWS EC2 Instances")
	os.system(" tput setaf 93 ")
	print("--------------------------------------------------------\n")

design1()
design2()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')

    elif hour>=12 and hour<18:
        speak('Good Afternoon') 
        
    else:
        speak('Good Night')

wishMe()
speak('Sir, Ziara here I am your voice assistant, Please tell me how may I help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\t\tI am listening....\n")
        speak(" Tell me your requirements......")
        r.pause_threshold = 1 
        audio = r.listen(source)
      
    try:
        print('\t\tRecognising....\n')
        speak("I got it, please wait.....")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        print('Say that again please...\n')
        speak('Say that again please...')
        return 'None'

    return query

while True:
        os.system(" cls" )
        design1() 
        design2()
        query = takeCommand().lower()

        if 'how are you' in query:
            speak('Sir, I am fine whats abut you')

        elif "you can do" in query:
            speak(" I have following services for you: ")
            os.system(" tput setaf 2 ")
            print(" Available Services are: ") 
            print("--------------------------------\n")

            speak(" All basic programs I can execute for you ")
            print("\t\t\t 1). All Basic Programs \n") 

            speak(" All Basic Linux Commands I can execute ")
            print("\t\t\t 2). Basic Linux  Commands \n") 

            speak(" AWS Cloud I can operate for you ")
            print("\t\t\t 3). AWS Cloud \n") 
  
            speak(" I will provide docker services to you ")
            print("\t\t\t 4). Docker Services \n") 
  
            speak(" I can configure ansible for you ")
            print("\t\t\t 5). Ansible Configuration \n") 
  
            speak(" I can configure entire hadoop cluster on AWS ")
            print("\t\t\t 6). Hadoop Services \n") 

            speak(" I can configure web server on the top of AWS ")
            print("\t\t\t 7). Web Server Configuration \n")
 
            speak(" I will provide you machine learning services ")
            print("\t\t\t 8). Machine Learning Services \n")

        elif "basic menu" in query:
            os.system(" python basic_menu.py ")
            os.system(" cls ")

        elif "docker menu" in query:
            os.system(" python docker_conf_menu.py ")
            os.system(" cls ")
            os.system(" python docker_cmd_menu.py ")
            os.system(" cls ")        
 
        elif 'exit' in query:
            print('Thankyou sir for using my services.')
            os.system(" tput setaf 35 ")
            print("-------------------------------------\n")
            speak('Thankyou sir for using my services')
            break

        else:
            print(" Please say the command again....\n")
            speak(" Please say the command again")	

        input(" Please enter to continue......\n")
        os.system(" tput setaf 99 ")
