#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date

expirydate = datetime.date(2021, 9, 15)
#expirydate = datetime.date(2021, 12, 30)
today=date.today()
period=20230111225
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(0.1)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(0.1)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    def getSum(n):
        sum=0
        for digit in str(n):
            sum+=int(digit)
        return sum

    clear()
    y=1
    
    newperiod=period
    banner='figlet RXCE'
   # thisway=[2,6,8,11,12,15,16,18,19,20]
   # thatway=[1,3,4,5,7,9,10,14,13,17]
    numbers=[]
    #i=1
    while(y):
        clear()
        system(banner)
        print("Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
       # def getSum(n):
        #    sum=0
         #   for digit in str(n):
         #       sum += int(digit)
          #  return sum   
        last2=str(current) [-2:1]  
        if(newperiod%2==0):
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1,"Green")
            else:
                print(newperiod+1,"GREEN")
        else:
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1,"RED")
            else:
                print(newperiod+1,"RED")
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n")
            #print(number)
if(expirydate>today):
    now=datetime.datetime.now()
    First=now.replace(hour=13,minute=1)
    Firstend=now.replace(hour=14)
    Second=now.replace(hour=16)
    Secondend=now.replace(hour=17)
    Third=now.replace(hour=15)
    Thirdend=now.replace(hour=16)
    Final=now.replace(hour=17)
    Finalend=now.replace(hour=18)
    if(now>Third and now<Thirdend):
        period=20230107437
        hero()
    elif(now):
        period=20230107437
        hero()
    elif(False):
        period=20230107337
        hero()
    elif(False):
        period=20230107337
        hero()
    else:
        banner="Rxce"
        system(banner)
else:
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

hero()

"""  if i in thisway:
            m=getSum(current)
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print(newperiod+1," : RED")
                else:
                    print(newperiod+1," : GREEN")
            else:
                if current in numbers:
                    print(newperiod+1," : GREEN")
                else:
                    print(newperiod+1," : RED")
        if i in thatway:
            m=getSum(current)+1
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print(newperiod+1,": RED")
                else:
                    print(newperiod+1,": GREEN")
            else:
                if current in numbers:
                    print(newperiod+1,": GREEN")
                else:
                    print(newperiod+1,": RED")
        i=i+1
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n")
            #print(numbers) """



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   