import requests
import discord
import os
import sys
import colorama
import threading
from itertools import cycle
from datetime import datetime
from colorama import Fore, init, Style
import ctypes
import urllib
import time
import keyboard


os.system("cls") #use this for windows. change to os.system("clear") for linux

#COLORS = {\
#"black":"\u001b[30;1m",
#"red": "\u001b[31;1m",
#"green":"\u001b[32m",
#"yellow":"\u001b[33;1m",
#"blue":"\u001b[34;1m",
#"magenta":"\u001b[35m",
#"cyan": "\u001b[36m",
#"white":"\u001b[37m",
#"yellow-background":"\u001b[43m",
#"black-background":"\u001b[40m",
#"cyan-background":"\u001b[46;1m",
#}





print('''\u001b[35m
  ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
  ████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
  ██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
  ██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
  ██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
  ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

• Made by  https://slimez.wtf/                          
            ''')


email = input('Email: ')
password = input('Password: ')
data={'email': email, 'password': password, 'undelete': "false"}
headers={'content-type': "application/json", 'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
r = requests.post('https://discord.com/api/v8/auth/login', json=data, headers=headers)
if r.status_code == 200:
        token = r.json()['token']
        print(f'Token: {token}')
       	input('Press Enter to Exit...')    
        if keyboard.is_pressed('enter'):
          os.system('cls')
elif "PASSWORD_DOES_NOT_MATCH" in r.text:
        print(f'{Fore.RED}Invalid Password{Fore.RESET}') #colorama fail Lmaoo, fuck colorama    
        input('Press Enter to Exit...')
        if keyboard.is_pressed('enter'):
          os.system('cls')
elif "captcha-required" in r.text:
        print(f'Discord Returned Captcha, Try Again Later')   
        input('Press Enter to Exit...')
        if keyboard.is_pressed('enter'):
          os.system('cls')
else:
      print(f'Invalid choice')
      input('Press Enter to Exit...')
      while True:
        if keyboard.is_pressed('enter'):
            pause()