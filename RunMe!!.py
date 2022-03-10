import time
import os
import sys

os.system('title Nightmare Beta V1.0.0')

pcname = (os.getenv('COMPUTERNAME'))

def printslow(text):
  for i in text:
    print(i,end="")
    sys.stdout.flush()
    time.sleep(0.06)
  print('')

printslow('Hello ' + pcname)
time.sleep(1)
printslow('Nightmare Tools Were Coded By Shade#3421 Steffke#0001 Dacki#0001 strxanger#001 And slimez#3883')
time.sleep(1)
printslow('Dont Be A Skid')
time.sleep(1)
printslow('So A Promblem I Have Ran Into Is That The Compiled Files Seems To Have Vendors On VirusTotal')
printslow('But Its Just Being Dumb You Can Decompile The File To See There Is No Trojan')
time.sleep(1)
printslow('Anyways Have Fun Using Nightmare Tools Beta V1.0.0 In The Next Version I will Try My Hardest') 
printslow('To Fix The VirusTotal Problem')
time.sleep(1)
printslow('Have A Great Rest Of Your Day ' + pcname)
input('Press Enter to Exit...')