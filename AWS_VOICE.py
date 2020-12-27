import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import os

pyttsx3.speak("Hello")
print()
print("WELCOME TO THE WORLD OF AUTOMATION".center(125))
pyttsx3.speak("WELCOME TO THE WORLD OF AUTOMATION".center(125))
pyttsx3.speak("Here I am going to automate AWS services for you ......")
pyttsx3.speak("How can i help you...?")


while True:
    print()

    r = sr.Recognizer()

    with sr.Microphone() as source:
        
        audio = r.listen(source)
        pyttsx3.speak('i got it... please wait..!!')

    ch = r.recognize_google(audio)
    print(ch)
    ch = ch.lower()
# Here i am giving command to create key pair

    if(("make" in ch) or ("create" in ch) and ("key pair" in ch)):
        pyttsx3.speak("Enter the name of the key pair")
        keyname = input("Enter the name of Key Pair:  ")
        
        os.system("aws ec2 create-key-pair --key-name {}".format(keyname))
        wb.open(
            'https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#KeyPairs:')
        pyttsx3.speak('Key pair created')
        input("Press enter to continue")


# security grp
    elif(("create" in ch) and ("security group" in ch)):
        pyttsx3.speak("Enter the name of security group:  ")
        groupname = input("Enter the name of security group:  ")
        pyttsx3.speak("Enter the description you want to give to your security group :  ")
        groupdescription = input(
            "Enter the description you want to give to your security group :  ")
        os.system("aws ec2 create-security-group --group-name {} --description {}".format(
            groupname, groupdescription))
        wb.open(
            'https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#SecurityGroups:')
        pyttsx3.speak('Security group created')
        input("Press enter to continue")

# ec2 instance launch
    elif(("create " in ch) or ("launch" in ch ) and ("ec2 instance" in ch) or ("new instance" in ch) or ("e c 2 instance" in ch)):
        pyttsx3.speak("Enter the image id ")
        imageid = input("Enter the image id: ")
        pyttsx3.speak("Enter the instance type you want to have: ")
        instance_type = input("Enter the instance type you want to have: ")
        pyttsx3.speak("Enter the number of instances you want to create ")
        instance_number = input(
            "Enter the number of instances you want to create: ")
        pyttsx3.speak("Enter the subnet id")
        subnet_id = input("Enter the subnet id: ")
        pyttsx3.speak("Enter the ids of security groups you want to provide: ")
        security_group = input(
            "Enter the ids of security groups you want to provide: ")
        pyttsx3.speak("Enter the key pair : ")
        keyname = input("Enter the key pair : ")
        os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}".format(
            imageid, instance_type, instance_number, subnet_id, security_group, keyname))
        wb.open(
            "https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
        pyttsx3.speak("I created a new instance for you")
        input("Press enter to continue")

        # ebs volume 
    elif(("create" in ch) and ("ebs volume" in ch)):
        pyttsx3.speak("Enter the availability zone you want to launch the ebs volume in")
        avail_zone = input(
            "Enter the availability zone you want to launch the ebs volume in")
        size = input("Enter the size of ebs volume")
        os.system(
            "aws ec2 create-volume --availability-zone {} --size {} --volume-type gp2".format(avail_zone, size))
        wb.open(
            "https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:sort=desc:createTime")
        pyttsx3.speak("I created an ebs volume for you")
        input("Press enter to continue")
        # instance start
    elif(("start" in ch) and ("instance" in ch)):
        pyttsx3.speak("Enter the id of instance which you want to start:  ")
        instance_id = input(
            "Enter the id of instance which you want to start:  ")
        os.system("aws ec2 start-instances --instance-ids {}".format(instance_id))
        wb.open(
            "https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
        pyttsx3.speak("I started the instance for you")
        input("Press enter to continue")
#  instance stop
    elif(("stop" in ch) and ("instance" in ch)):
        pyttsx3.speak("Enter the id of instance which you want to stop:  ")
        instance_id = input(
            "Enter the id of instance which you want to stop:  ")
        os.system("aws ec2 stop-instances --instance-ids {}".format(instance_id))
        wb.open(
            "https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
        pyttsx3.speak("I stopped the instance for you")
        input("Press enter to continue")
#  instance terminate
    elif(("terminate" in ch) and ("instance" in ch)):
        pyttsx3.speak("Enter the id of instance which you want to terminate:  ")
        instance_id = input(
            "Enter the id of instance which you want to terminate:  ")
        os.system(
            "aws ec2 terminate-instances --instance-ids {}".format(instance_id))
        wb.open(
            "https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
        pyttsx3.speak("I terminated the instance for you")
        input("Press enter to continue")
    elif(("attach ebs volume" in ch) and ("instance" in ch)):
        pyttsx3.speak("Enter the id of instance to which you want to attach an ebs volume:  ")
        instance_id = input(
            "Enter the id of instance to which you want to attach an ebs volume:  ")
        pyttsx3.speak("Enter the id of the volume that you want to attach to the instance:  ")
        volume_id = input(
            "Enter the id of the volume that you want to attach to the instance:  ")
        os.system(
            "aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volume_id, instance_id))
        wb.open(
            "https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
        pyttsx3.speak("The ebs volume has been attached to the instance")
        input("Press enter to continue")
    elif(("detach ebs volume" in ch) and ("" in ch)):
        pyttsx3.speak("Enter the id of the volume that you want to detach:  ")
        volume_id = input(
            "Enter the id of the volume that you want to detach:  ")
        os.system("aws ec2 detach-volume --volume-id {}".format(volume_id))
        wb.open(
            "https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
        pyttsx3.speak(
            "The ebs volume has been detached from the instances that it was attached to")
        input("Press enter to continue")
    elif("create s3 bucket" in ch):
        pyttsx3.speak("Enter the name you want to give to the new s3 bucket")
        name = input("Enter the name you want to give to the new s3 bucket")
        os.system("aws s3 mb s3://{}".format(name))
        wb.open("https://s3.console.aws.amazon.com/s3/home?region=ap-south-1#")
        pyttsx3.speak("S3 bucket has been created")
        input("Press enter to continue")
    pyttsx3.speak("Tell me ur next requirement")