#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:50:29 2023

@author: marion
"""

#EXAMS : 60% Midterm and 40% project : Last week of november for the project, 1 week to finish it
#Project : You need a code with comments and everything, a document and 2-5 minutes video of yourself explaining the code. 
#It can be done in teams or alone
#Midterm : 5 to 7 problems


#datacamp


sum=0
count=0
list=[]
n=0

n=input("Enter a value :")

while n!="":
    
        n=int(n)
        sum=sum+n
        count=count+1
        list.append(n)
        n=input("Enter a value :")
    

if count==0:
    print("The list is empty")
    
else:

 print("The list of values is {}".format(list))
 print("The mean of the list is {}".format(sum/count))
 
 #%%
 
names=input(("Enter a list of names separated by blanks : "))
 
if names=="":
    
    print("There are 0 people in the list")
    
else:
 
 names_list=names.split(" ")
 n=len(names_list)
 print(names_list)
 
 
 for name in names_list :
  print("Hi {}".format(name))
 
 print("Welcome all {}".format(len(names_list)))
    
#%%



symbols=("H","C","N","O","S","Cl")
mass=(1.008,12.011,14.007,15.999,32.065,35.453)
total=0

for i in range (len(symbols)) : #IF YOU WANT TO USE THE LENGTH YOU HAVE TO PUT IT IN PARENTHESIS
    n=int(input("How many atoms of {} ? :".format(symbols[i])))
    total=total+(n*mass[i])
    
print("The mass of the molecule is {:.3f} u".format(total))

#%%
n=int(input("What is the maximum degree of the polynomial ? :"))
poly=[]

for i in range(n+1):
    v=int(input("What is the coefficient of x^{} ?".format(i)))
    poly.append(v)
    
    
x=float(input("What is the value of x ? :"))
total=poly[0]
for i in range(1,n+1):
    total=total+poly[i]*(x**i)
    
print("The value of the polynomial for x={} is {}".format(x,total))

#%%

#Functions 

# def function_name (argument):
    #content of the function
    #return value

def hf():
    print("Hello World")

hf()

def add(x,y):
    c=x+y
    print(c)
    
add(1,2)

def hello(wish):
    return '{}'.format(wish.upper())
print(hello("mrcet"))


#if you have a default argument (where you don't specify a value, it has to be first)

def func(a,b=10,c=100): #a is undefined but it works because it's in first position
    print('a is',a,'and b is',b,'and c is',c)
    return a,b,c

def funct(a=10):# a is defined but it works as well because there are no undefined variables after
    print('a is',a)
    return a
funct()

# def function(a=10,b) wouldn't work 

#%%

#Variable-length argument

def wish(*names): #*argw, **kwargs
 names=("MRCET","CSE","SIR","MADAM")
 for name in names:
     print("Hello",name)
    




    
    
 

     
     
     
     

