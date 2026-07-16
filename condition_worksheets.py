# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:30:00 2026

@author: VICTUS
"""
#Condition worksheets:
#Q1:
num1=int(input("put the first number:"))
num2=int(input("put the second number:"))
if(num1>num2):
    print(f"{num1} is graeter than {num2}")
elif (num1<num2):
    print(f"{num1} is less than {num2}")
else:
    print("num1 and num2 are equals")
#%%
#Q2:
incom=int(input("Please enter your incom :"))

if incom< 50000:
    tax=0.01
    print("The tax is :",tax)
elif incom>=50000 and incom<=10000:
    tax=0.02
    print("The tax is :",tax) 
else :
    tax=0.03
    print("The tax is :",tax)
#%%
#Q3:
height=int(input("Please enter your height :"))
weight=int(input("Please enter your weight :"))
height=height/100
BMI=(weight/(height**2))
if (BMI<18.5):
    print("Underweight")
elif(BMI>=18.5 and BMI<25):
    print("Normal")
elif(BMI>=25 and BMI <30):
    print("Overweight")
else:
    print("Obese")
#%%
#Q4:

x=int(input("ENTER THE NUMBER :"))
y=int(input("ENTER THE NUMBER :"))
z=int(input("ENTER THE NUMBER :"))
if (x<=y and x<=z):
    Min=x
    if(y<=z):
        mid=y
        Max=z
    else:
        mid=z
        Max=y
elif (y<x and y<=z ):
    Min=y
    if(x<=z):
        mid=x
        Max=z
    else:
        mid=z
        Max=x
else:
    Min = z
    if (x <= y):
        mid = x
        Max = y
    else:
        mid = y
        Max = x

print(Min, mid, Max)
        




        
    





#%%
#Q5:
day=int(input("Enter  number of day :"))

if  day==1:
    print("The day is Sunday")
elif day==2:
    print("The day is Monday")
elif day==3:
    print("The day is Tuesday")
elif day==4:
    print("The day is Wedensday")
elif day==5:
    print("The day is Thursday")
elif day==6:
    print("The day is Friday")
elif day==7:
    print("The day is saturday")
else:
    print("The number out of range,Tru again ")
#%%
#Q6:
player1=input(" player1 input Rock or Scissors or paper:").lower()
player2=input(" player2 input Rock or Scissors or paper:").lower()
if(player1==player2):
     print("They are a same . try again ")
     
     
elif (player1=="rock" and player2=="scissors"):
    print("player1 is winnn")
elif (player1=="scissors"and player2=="paper"):
    print("Player1 is winnn")

     
else:
    print("player2 is winnn")
    

#%%
# Q7:
person_age=int (input("Enter your age :"))
if person_age>=0 and person_age<=12:
    print("Child")
elif person_age>=13 and person_age<=19:
    print("Teen")
elif person_age >=20 and person_age<=59:
    print("Adult")
elif person_age>60:
    print("Senior")
#%%
# Q8:
letter =input("Enter letter to check is a vowel or constant:")
vowel=(letter=="A" or letter =="a" or 
    letter=="E" or letter=="e" or 
    letter=="I" or letter=="i" or 
    letter=="O" or letter=="o" or 
    letter=="U" or letter=="u")
y=(letter=="y" or letter=="Y")
if (vowel):
    print("The letter is vowel")
elif (y):
    print(" This letter sometimes is a vowel and sometimes is a constant ")
else :
    print("The letter is a constant ")
          
    

    









      























