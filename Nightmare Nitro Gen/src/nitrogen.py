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
import random
import json
import string


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
            
            
try:
      amount = int(input(f'[?] Amount: '))
      value = 1
      while value <= amount:
        code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        f = open(f'Nitro codes ({amount}).txt', "a+")
        f.write(f'{code}\n')
        f.close()
        print(f'{code}')
        value += 1
      print('')
      input('Press Enter to Exit...')
except ValueError:
      print(f'Invalid choice')
      input('Press Enter to Exit...')