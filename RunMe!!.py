import time
import os
import sys

os.system('title Nightmare Beta V1.0.1')

pcname = (os.getenv('COMPUTERNAME'))

def printslow(text):
  for i in text:
    print(i,end="")
    sys.stdout.flush()
    time.sleep(0.06)
  print('')

printslow('Hello ' + pcname)
time.sleep(1)
printslow('Nightmare Tools Were Coded By Shade#3421 Steffke#0001 Dacki#0001 strxanger#0001 And slimez#3883')
time.sleep(1)
printslow('Dont Be A Skid')
time.sleep(1)
printslow('The Boys Sites https://shade.army https://slimez.wtf https://strxanger.org https://x10.wtf')
printslow('Added: ')
printslow('Nightmare Mass DM')
printslow('')
printslow('Have A Great Rest Of Your Day ' + pcname)
input('Press Enter to Exit...')