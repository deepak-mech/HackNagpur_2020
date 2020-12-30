import os
import pyttsx3
import speech_recognition as sr
import webbrowser

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
        print("=============================================================================================================================================================")
        os.system(" tput  setaf 1 ") 
        print("\t\t\t\t----------------->Your welcome in this Docker Automation Menu Program<----------------\t\t")
        os.system(" tput  setaf 3 ")
        print("=============================================================================================================================================================\n")
        os.system(" tput setaf 77 ")

def design2():
        os.system(" tput setaf 68 ")
        print(" Docker Basic Commands Menu Program ")
        print(" ------------------------------------------------\n")
        os.system(" tput setaf 78 ") 

def docker():
	print("""
	\t--------> Check Docker Version
	\t--------> Docker Info
	\t--------> Display Multiple Commands
	\t--------> Show all Docker Images
	\t--------> Check all Stopped/Running Containers
	\t--------> Show Container's ID
	\t--------> Remove all Containers
	\t--------> Remove all Images
	\t--------> Show Insights of Docker
	\t--------> Stop Docker Service
	\t--------> Uninstall Docker
	\t--------> Go Back to Main Menu
	""")

design1()
design2()
docker()
                                   
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
        #print(query)

    except Exception as e:
        print(e)
        print('Say that again please...\n')
        speak('Say that again please...')
        return 'None'

    return query

ip = input("Enter IP address where you want to remote login :  ")
print()
k_name = input("Enter the name of private key:  ")

while True: 
	os.system('cls')  
	design1()
	design2()
	docker()
	query = takeCommand().lower()

	if "version" in query:
		os.system(' ssh -i {}.pem root@{} docker -v '.format(k_name, ip))
		print()

	elif "info" in query:
		os.system( " ssh -i {}.pem root@{} docker info ".format(k_name, ip))
		print()

	elif "multiple" in query:
		os.system(" ssh -i {}.pem root@{} docker help ".format(k_name, ip))
		print()

	elif "all docker images" in query:
		os.system(" ssh -i {}.pem root@{} docker images ".format(k_name, ip))
		print()

	elif "containers status" in query:
		os.system(" ssh -i {}.pem root@{} docker ps -a ".format(k_name, ip))
		print()

	elif "show containers id" in query:
		os.system(" ssh -i {}.pem root@{} docker ps -a -q ".format(k_name, ip))
		print()

	elif  "remove all containers" in query:
		os.system(" ssh -i {}.pem root@{} docker rm `docker ps -a -q` ".format(k_name, ip))
		print()

	elif  "remove all images" in query:
		os.system(" ssh -i {}.pem root@{} docker rmi `docker ps -a -q` ".format(k_name, ip))
		print()

	elif "insights" in query:
		cont_name = input(" Enter the name of container:  ")
		os.system(" ssh -i {}.pem root@{} docker logs {} ".format(k_name, ip, cont_name))
		print()

	elif "stop docker service" in query:
		os.system( " ssh -i {}.pem root@{} systemctl stop docker ".format(k_name, ip))
		os.system( " ssh -i {}.pem root@{} systemctl status docker ".format(k_name, ip))
		print("\t\t\t___________________________________________")
		os.system(" tput setaf 2 ")
		print(' \t\t\t\tDocker Services Stopped ')
		os.system(" tput setaf 23 ")
		print("\t\t\t___________________________________________\n")
		speak(" Docker Services Stopped ")

	elif "uninstall docker" in query:
		os.system( " ssh -i {}.pem root@{} yum remove docker-ce -y ".format(k_name, ip))
		os.system( " ssh -i {}.pem root@{} rpm -q docker-ce ".format(k_name, ip))
		print("\t\t\t___________________________________________")
		os.system(" tput setaf 2 ")
		print(' \t\t\t\tDocker Is Uninstalled ')
		os.system(" tput setaf 23 ")
		print("\t\t\t___________________________________________\n")
		speak(" Docker is uninstalled ")

	elif "main menu" in query:
		print(" \t\t\t\t Go back to main menu...")
		speak(" Go back to main menu ")
		break

	else:
		print(" Please say the command again....")
		speak(" Please say the command again")	

	os.system(" tput setaf 19 ")
	input(" \t\t\t\tPress Enter to Continue......")







