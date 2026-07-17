# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:08:46 2026

@author: VICTUS
"""

#Loop Ecxrsise:
#Q1:
num=1
while(num!=11):
    print(num)
    num+=1
#%%
#Q2:
for i in range(1,6):
    for j in range(1,i+1) :
        print(j,end=" ")
    
    print("\n")
        
#%%
#Q3:
summ=0
num=int(input("Enter the numbers :"))       
while(num!=0):
    summ+=num
    num=int(input("Enter the numbers :"))
print("sum of numbers =", summ)
#%%
#Q4:
for i in range (1,11):
    print("\n")
    for j in range (1,11):
        print(i,"*",j,"=",i*j,sep="\t")
        
#%%  
#Q5:
x=75869432
count=0
while(x>0):
    count+=1
    x=x//10
    
print(count)
    



#%%
#Q6:
for i in range (-10,-0,1):
    print(i)
#%%
#Q7:
num=int(input("Enter numbers :"))

list1=[]

while (num!=0):
    list1.append(num)
    num=int(input("Enter numbers :"))
    
    
print(list1)
summ=sum(list1)
lenn=len(list1)
avg=summ/lenn
print(avg)
    
    
