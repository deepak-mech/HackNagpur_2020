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
        print("=============================================================================================================================")
        os.system(" tput  setaf 1 ") 
        print("\t\t\t\t----------------->Your welcome in this Docker Automation Menu Program<----------------\t\t")
        os.system(" tput  setaf 3 ")
        print("=============================================================================================================================\n")
        os.system(" tput setaf 77 ")

def design2():
        os.system(" tput setaf 68 ")
        print(" Docker Configuration Menu Program ")
        print(" --------------------------------------\n")
        os.system(" tput setaf 78 ")      

def docker():
	print("""
	\t---------> Configure Yum for Docker
	\t---------> Install Docker
	\t---------> Start Docker Service
	\t---------> Pull Docker Image 
	\t---------> Launch & Start Docker Container
	\t---------> Stop the Container
	\t---------> Restart the Container
	\t---------> Docker Basic Commands Menu
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

	if "yum" in query:
		os.system(' echo [docker2] >> docker.repo ')
		os.system(' echo baseurl = https://download.docker.com/linux/centos/7/x86_64/stable >> docker.repo ')
		os.system(' echo gpgcheck = 0 >> docker.repo ')
		os.system(' scp -i {}.pem docker.repo root@{}:/etc/yum.repos.d/  '.format(k_name, ip))
		os.system('  ssh -i {}.pem root@{} yum list docker-ce '.format(k_name, ip))
		os.system(' rm -rf  docker.repo ' )
		print("\t\t\t___________________________________________")
		os.system(" tput setaf 23 ")
		print(' \t\t\t\tYum Configured Successfully ')
		os.system(" tput setaf 18 ")
		print("\t\t\t___________________________________________\n")
		speak(" Yum Configured Successfully ")
	

	elif "install" in query:
		os.system( "  ssh  -i  {}.pem  root@{}  yum install docker-ce  --nobest  -y ".format(k_name, ip))
		os.system("  ssh -i {}.pem root@{} rpm -q docker-ce ".format(k_name, ip))
		print("\t\t\t___________________________________________")
		os.system(" tput setaf 2 ")
		print(' \t\t\t\tDocker Installed Successfully ')
		os.system(" tput setaf 19 ")
		print("\t\t\t___________________________________________\n")
		speak(" Docker Installed Successfully ")

	elif "start docker service" in query:
		os.system( " ssh -i {}.pem root@{} setenforce 0 ".format(k_name, ip))
		os.system( " ssh -i {}.pem root@{} systemctl start docker ".format(k_name, ip))
		os.system( " ssh -i {}.pem root@{} systemctl status docker ".format(k_name, ip))
		print("\t\t\t___________________________________________")
		os.system(" tput setaf 2 ")
		print(' \t\t\t\tDocker Services Started ')
		os.system(" tput setaf 23 ")
		print("\t\t\t___________________________________________\n")
		speak(" Docker Services Started ")

	elif  "pull" in query:
		img_name = input("Enter the name of image:  ")
		os.system(" ssh -i {}.pem root@{} docker pull {}  ".format(k_name, ip, img_name))
		os.system(' ssh -i {}.pem root@{} docker images '.format(k_name, ip))
		print("\t\t\t___________________________________________")
		os.system(" tput setaf 23 ")
		print(' \t\t\t\tImages Pulled Successfully ')
		os.system(" tput setaf 18 ")
		print("\t\t\t___________________________________________\n")
		speak(" Images Pulled Successfully ")

	elif "launch" in query:
		cont_name = input('Enter the name of container:  ')
		img_name = input("Enter the name of image:  ")
		os.system(" ssh -i {}.pem root@{} docker run -dit --name {} -p 8080:80 {} ".format(k_name, ip, cont_name, img_name))
		os.system(' ssh -i {}.pem root@{} docker ps '.format(k_name, ip))
		print("\t\t\t___________________________________________")
		os.system(" tput setaf 2 ")
		print(' \t\t\t\tDocker Launched Successfully ')
		os.system(" tput setaf 19 ")
		print("\t\t\t___________________________________________\n")
		speak(" Docker Launched Successfully ")

	elif "stop the container" in query:
		cont_name = input(' Enter the name of container:  ')
		os.system(' ssh -i {}.pem root@{} docker stop {} '.format(k_name, ip, cont_name))
		os.system(' ssh -i {}.pem root@{} docker ps '.format(k_name, ip))
		print()
		print("\t\t\t\t Stopping Container....\n")
		speak(" Stopping Container ")

	elif "restart the container" in query:
		os.system(' ssh -i {}.pem root@{} docker start {} '.format(k_name, ip, cont_name))
		os.system(' ssh -i {}.pem root@{} docker ps '.format(k_name, ip))
		print("\t\t\t\t Restarting Container....\n\n")
		speak(" Restarting Container ")
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

	elif "basic" in query:
		os.system(" tput setaf 2 ")
		print(" \t\t\t\t Opening Docker Basic Commands Menu...")
		speak(" Opening Docker Basic Commands Menu ")
		break

	else:
		print(" Please say the command again....")
		speak(" Please say the command again")	
	
	os.system(" tput setaf 4 ")
	input(" \t\t\t\tPress Enter to Continue......")



