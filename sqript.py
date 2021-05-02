import random
import time
import math
import os
import webbrowser

def tak ():
 os.system('clear')
 print('\t\033[0;32mwelkom to my sqript 2021')
 time.sleep(1)
 print('\t\033[0;31mloading..')
 time.sleep(1)
 print('\t\033[0;33mcomplet\n')
 print('|1|:\033[0;31mlen to to text')
 print('|2|:compile passward higt')
 print('|3|:open site link ')
 print('|10|:again')
 a=int(input('#'))
 if a==1 :
   kahf()
 elif a==2 :
   code()
 elif a==3:
   open()
 else:
   tak()
def kahf():
 os.system('clear')
 print('loading...\n')
 time.sleep(1)
 print(( 'hello to recherche un mont dons text\n').center(30));(),((()));
# ecrire (hhhhh) lire a, Hhhhhh....
 while True:
   a=input(' \033[0;35mentre text:')
   b=input(' \033[0;33mentre le mont:')
   if a ==('a') or b==('a') :
   	tak()     
   v=a.count(b);#hhhhhhhhh im pro 
   print('  \033[0;36m',v),((((((('')))))));
   v=(('\ANONYMOS!\!'.center((30))));
   print('\033[0;32m',v)#Haker mohamed vip!
   print(((('\033[0;36m|a|:again'))));
def code():
 os.system('clear')
 while True:
  print('loading...')
  time.sleep(1)
  a=input('\033[0;33menter your normal code :')
  if a==('a'):
  	tak()
  b=len(a)
  print('your len et: ',b,'\n')
  moha="".join(random.sample(a,b))
  print('code combile et : ',moha,'\n')
  print('|a|:again')
def open():
  os.system('clear')
  print('\033[0;91mloading......')
  time.sleep(2)
  print('\033[0;31m        ──▒▒▒▒▒▒▒▒───▒▒▒▒▒▒▒▒ ─▒▐▒▐▒▒▒▒▌▒─▒▒▌▒▒▐▒▒▌▒ ──▒▀▄█▒▄▀▒───▒▀▄▒▌▄▀▒ ─────██─────────██ ░░░▄▄██▄░░░░░░░▄██▄░░░   ')
  time.sleep(0.5)
  print('\033[0;32m──▒▒▒▒MoHaMeD▒Hichame▒▒▒───▒▒▒▒▒▒▒▒ ─▒▐▒▐▒▒▒▒▌▒▒▒▌▒▒▐▒▒▌▒ ──▒▀▄█▒▄▀▒───▒▀▄▒▌▄▀▒ ─────██─────────██ ░░░▄▄██▄░░open_site░░░░░▄██▄░░░')
  time.sleep(0.5)
  print('\033[0;31m        ──▒▒▒▒▒▒▒▒───▒▒▒▒▒▒▒▒ ─▒▐▒▐▒▒▒▒▌▒─▒▒▌▒▒▐▒▒▌▒ ──▒▀▄█▒▄▀▒───▒▀▄▒▌▄▀▒ ─────██─────────██ ░░░▄▄██▄░by-Mohamed░░░░░░▄██▄░░░   \n')
  b=input('\033[0;37menter lien de site:\033[0;36m')
  if b==('a'):
     tak()
  print('|a|again')
  time.sleep(0.5)
  while (True):
   time.sleep(0.5)
   a=webbrowser.open(b)

 
tak()
