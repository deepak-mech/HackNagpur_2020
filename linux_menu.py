import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import os

def design1():
        os.system(" cls ")    
        print("====================================================================================================================================================")

        print("\t\t\t\t----------------->Your welcome in this Linux Basic Commands Automation Menu Program<----------------\t\t")     
        print("===================================================================================================================================================\n")
        pyttsx3.speak("Your welcome in this  Linux Basic Commands Automation Menu Program")
      
def design2():
     
        print(" Linux Basic Commands SERVICES ")
        print(" ------------------------------------------------\n")
     

def basic_linux():
	print("""
	\t--------> Open Text editor
	\t--------> Open Vi Editor
	\t--------> To see the date and time
	\t--------> To see the Calender
	\t--------> To see the hard disk information
	\t--------> To ask query about any software
	\t--------> To download and install any software
	\t--------> To Open the file explorer
	\t--------> To open the terminal window
	\t--------> To audio player
        \t--------> To open the settings
	\t--------> To open Camera
	\t--------> To open the Calculator
	\t--------> To open the Video Player
	\t--------> To see the partition and mount information
	\t--------> To see the RAM information
	\t--------> To go inside a folder
	\t--------> To delete a directory
	\t--------> To delete a file 
	\t--------> To start a service
        \t--------> To stop a service
	\t--------> To enable a service
	\t--------> To disable a service
        \t--------> To see the files in present working directory
	\t--------> To see the IP of domain
	\t--------> To check the connectivity of IP
	\t--------> To transfer the file to other Linux System
	""")

design1()
design2()
basic_linux()

ip = "52.66.236.142"
pem = input("Enter the path of the .pem file")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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
        ch = r.recognize_google(audio, language='en-in')

    except :
        print('Say that again please...\n')
        speak('Say that again please...')
    return ch


while True:
	os.system(" cls" )
	design1() 
	design2()
	basic_linux()
	ch = takeCommand().lower()

	if ("text editor" in ch):
		file_name=input("Enter file name to open a file otherwise press Enter:")
		os.system("ssh -i {} ec2-user@{}  gedit  {} ".format(pem , ip , file_name))

	elif ("open vi editor"in ch):
 		print("Enter file name :")
 		file_name = input()
 		os.system("ssh -i {} ec2-user@{}  vi  {}".format(pem , ip , file_name))

	elif ( "date" in ch ):
		os.system("ssh -i {} ec2-user@{}  date ".format(pem , ip ))

	elif ( "calendar" in ch or "calender" in ch):#calender
		os.system("ssh -i {} ec2-user@{}  cal ".format(pem , ip ))
 	
	elif ("open hard disk info "in ch):
 		# OPEN harddisk info
 		os.system("ssh -i {} ec2-user@{}  fdisk -l".format(pem,ip))

	elif ("query about software "in ch):
 		# ask Query about Software
 		print("Enter Software name :")
 		sft_name = input()
 		os.system("ssh -i {} ec2-user@{}  rpm -q  {}".format(pem,ip,sft_name))

	elif ("Download software and install " in ch ):
 		# Download Software and install 
 		print("Enter a link:")
 		link = input()
 		os.system("ssh -i {} ec2-user@{} yum install  {}".format(pem ,ip,link))

	elif ("open file explorer "in ch):
		# open file explorer
 		os.system("ssh -i {} ec2-user@{} nautilus &".format(pem,ip))

	elif ("open terminal window" in ch):
 		#open Terminal Window
 		os.system("ssh -i {} ec2-user@{} gnome-terminal &".format(pem,ip))

	elif ("open audio player " in ch):
 		# open Audio player
 		os.system("ssh -i {} ec2-user@{}  rhythmbox &".format(pem,ip))

	elif ("open setting" in ch):
 		# open setting
 		os.system("ssh -i {} ec2-user@{}  gnome-control-center &".format(pem,ip))
 		
	elif ("open calculator" in ch):
 		# open calculator
 		os.system("ssh -i {} ec2-user@{}  gnome-calculator &".format(pem,ip))
 		
	elif ("open videoplayer" in ch):
 		# open videoplayer
 		os.system("ssh -i {} ec2-user@{} totem  &".format(pem,ip))

	elif ("see partition and mount information " in ch):
 		# See All Partition and Mount info
 		os.system("ssh -i {} ec2-user@{} lsblk".format(pem,ip))
 		
	elif ("see the ram information"in ch):
 		# see ram info
 		os.system("ssh -i {} ec2-user@{} free -m".format(pem,ip))

	elif ("to go inside a folder"in ch):
 		# go inside a folder
 		print("Enter your Path:")
 		path = input()
 		os.system("ssh -i {} ec2-user@{} cd {}".format(pem ,ip,path))

	elif ("to delete a directory"in ch):
 		# deleting Dirctory
 		print("Enter your Directory Name:",'yellow',end='')
 		dir_name = input()
 		os.system("ssh -i {} ec2-user@{} rm -rf {}".format(pem,ip,dir_name))

	elif ("to delete a file"in  ch ):
 		# deleting File
 		print("Enter your File Name:")
 		dir_name = input()
 		os.system("ssh -i {} ec2-user@{} rm  {}".format(pem,ip,dir_name))	
			
	elif ("start" in ch) :
 		# start a service
		service = input("Enter the service name you want to start")
		os.system("ssh -i {} ec2-user@{} sudo systemctl start httpd".format(pem,ip))
		print("Successfully started")

	elif ("to stop a service "in ch) :
 		# stop a service
 		print("Enter service name:")
 		service = input()
 		os.system("ssh -i {} ec2-user@{} systemctl stop {} ".format(pem,ip,service))

	elif ("to enable a service "in ch)  :
 		# enable a service
 		print("Enter service name:")
 		service = input()
 		os.system("ssh -i {} ec2-user@{} systemctl enable {} ".format(pem,ip,service))

	elif ("to disable a service"in ch):
 		# disable a service
 		print("Enter service name:")
 		service = input()
 		os.system("ssh -i {} ec2-user@{} systemctl disable {} ".format(pem,ip,service))
				
	elif  ("to see the files in present working directory"in ch):
 		# See files of present Directory
 		os.system("ssh -i {} ec2-user@{} ls".format(pem,ip))
			
	elif ("to see IP of domain" in ch):
 		# To SEE IP OF Domain 
 		os.system("ssh -i {} ec2-user@{} ifconfig".format(pem,ip))

	elif ("to check the connectivity to IP" in ch ):
 		# To Check Connectivity to ip
 		print("Enter Ip to check connectivity:")
 		it = input()
 		os.system("ssh -i {} ec2-user@{} ping -c 4 {} ".format(pem,ip,it))

	elif ("to transfer the file to other Linux System"in ch):
 		#Transfer file to other linux system
 		it = input("Enter ip of system to which you want to Send file:  ")
 		print("Enter username  to which you want to Send file:")
 		usr = input()
 		print("Enter source file path which you want to Send :")
 		source = input()
 		cprint("Enter destination path to where you want to Send file:")
 		destination = input()
 		os.system("ssh -i {} ec2-user@{} scp {} {}@{}:{} ".format(pem,ip,source,usr,it,destination))

	else:
		print("\n Please say the command again....\n")
		speak(" Please say the command again")	

	input(" Please enter to continue......\n")
	os.system(" tput setaf 99 ")
		    	
