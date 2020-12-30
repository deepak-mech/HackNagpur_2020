import os
import pyttsx3
import speech_recognition as sr

def design1():
		os.system(" cls ")
		print("=============================================================================================================================================================")

		print("\t\t\t\t----------------->Your welcome in this Hadoop Automation Menu Program<----------------\t\t")
		pyttsx3.speak("Your welcome in this Hadoop Automation Menu Program")
		
		print("=============================================================================================================================================================\n")
		
def design2():		
		print("HADOOP SERVICES ")
		print(" ------------------------------------------------\n")
		
def hadoop():
		print("""
		\t--------> Install java
		\t--------> Install hadoop
		\t--------> Configure data node
		\t--------> Configure master node
		\t--------> Start name node
		\t--------> Stop name node
		\t--------> Start data node
		\t--------> Stop data node
		\t--------> Hadoop Admin report
	""")

design1()
design2()
pyttsx3.speak("Are you sure that you have rpm file of hadoop and java ")
a = input("Are you sure that you have rpm file of hadoop and java [yes/no] :  ")
b = 'yes'
if a != b:
		os.system("tput setaf 9")
		print("First get that file : ")
		pyttsx3.speak("First get that file :")
		exit()

pyttsx3.speak("Tell me your requirements...........I 'm listening to you ")

while True:
        
	design2()
	hadoop()
	r = sr.Recognizer()

	with sr.Microphone() as source:

		audio = r.listen(source)
		pyttsx3.speak('i got it... please wait..!!')
	try:
		ch = r.recognize_google(audio)
		print(ch)
		ch = ch.lower()

	except Exception as e:
		print(e)
		print('Say that again please...\n')
		pyttsx3.speak('Say that again please...')

	if ("configure name node" in ch or "namenode"in ch):
		
		os.system("ssh -i Hadoop.pem ec2-user@52.66.236.142 sudo rpm -ivh /root/jdk-8u171-linux-x64.rpm")
		os.system("ssh -i Hadoop.pem ec2-user@52.66.236.142 sudo rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")

		os.system("ssh -i Hadoop.pem ec2-user@52.66.236.142 sudo rm /etc/hadoop/core-site.xml -y")
		os.system("ssh -i Hadoop.pem ec2-user@52.66.236.142 sudo rm /etc/hadoop/hdfs-site.xml -y")

		os.system("ssh -i Hadoop.pem ec2-user@52.66.236.142 sudo cp /core-site.xml /etc/hadoop/")
		os.system("ssh -i Hadoop.pem ec2-user@52.66.236.142 sudo cp /hdfs-site.xml /etc/hadoop/")

		os.system("ssh -i Hadoop.pem ec2-user@52.66.236.142 sudo hadoop namenode -format -y")
		os.system("ssh -i Hadoop.pem ec2-user@52.66.236.142 sudo hadoop-daemon.sh start namenode")		
		print("Name Node configured and started successfully")

	elif ("configure data node" in ch or "dataNode" in ch):
		os.system("ssh -i Hadoop.pem ec2-user@15.207.21.81 sudo rpm -ivh /root/jdk-8u171-linux-x64.rpm")
		os.system("ssh -i Hadoop.pem ec2-user@15.207.21.81 sudo rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force")

		os.system("ssh -i Hadoop.pem ec2-user@15.207.21.81 sudo rm /etc/hadoop/core-site.xml -y")
		os.system("ssh -i Hadoop.pem ec2-user@15.207.21.81 sudo rm /etc/hadoop/hdfs-site.xml -y")

		os.system("ssh -i Hadoop.pem ec2-user@15.207.21.81 sudo cp /root/core-site.xml /etc/hadoop/")
		os.system("ssh -i Hadoop.pem ec2-user@15.207.21.81 sudo cp /root/hdfs-site.xml /etc/hadoop/")

		os.system("ssh -i Hadoop.pem ec2-user@15.207.21.81 sudo hadoop-daemon.sh start datanode")
		print("Data Node configured and started successfully")

	else:
		print("Didn't work")
	input("Enter to continue")