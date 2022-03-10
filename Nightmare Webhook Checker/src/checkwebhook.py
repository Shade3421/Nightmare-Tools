import requests
import os
import sys
import threading
import ctypes
import urllib



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

webhook = input(f'\n[?] Webhook: ')
message = ('Test')
try:
    _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
    if _data.status_code < 400:
      print(f'\nWebhook valid')
      input('Press Enter to Exit...')
except:
    print(f'\n[?] Webhook valid')
    input('Press Enter to Exit...')