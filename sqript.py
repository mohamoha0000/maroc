import random
from turtle import *
import time
import math
import os
def tak ():
 print('\t\033[0;32mwelkom to my sqript 2021')
 time.sleep(1)
 print('\t\033[0;31mloading..')
 time.sleep(0.5)
 print('\t\033[0;33mcomplet\n')
 print('1:len to to text |2:compile password higt | 3:turtle joli | 4 : again')
 a=input()
 if a==1 :
    kahf()
 elif a==2 :
    code()
 elif a==3 :
    bag()
 else :
    os.system('clear')
    tak()
    
     
def kahf():
 print(('اهلا بك في تطبيق كشف عدد الكلمات في النص '.center(30)));(),((()));
# ecrire (hhhhh) lire a, Hhhhhh....
 while True:
   a=input(' \033[0;35mentre text:')
   b=input(' \033[0;33mentre le mont:')
   v=a.count(b);#hhhhhhhhh im pro 
   print('  \033[0;36m',v),((((((('')))))));
   v=(('\ANONYMOS!\!'.center((30))));  print('\033[0;32m',v)#Haker mohamed vip!
   print(((('\033[0;31m'))));

def code():
 while True:
  a=input('enter your normal code :')
  b=len(a)
  print('your len et: ',b,'\n')
  moha="".join(random.sample(a,b))
  print('code combile et : ',moha,'\n')
def bag ():
 a=[
'red','blue','orange','green','black','yellow'
]
 width(3)
 write('by:mohamed')
 while True:
  right(170)
  forward(250)
  time.sleep(0.5)
  b="".join(random.sample(a,1))
  bgcolor(b)
tak()

