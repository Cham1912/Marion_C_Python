#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:13:40 2023

@author: marion
"""

def helloworld():
    pass #if you have a function you don't want to use, you can use pass. And then you can change it later 
    
#Arguments 
#You can pass multiple arguments in a function 

#The argument is what you pass when calling your function.
#The parameters are what is between the parenthesis in the line where you declare your function 

def my_function(fname,lname):
    print(fname+" "+lname)
    
my_function("Emil","Jean")
#The amount of arguments and parameters have to be the same. Takes lists and tuples as inputs 

#*args : Taking multiple inputs

def my_function(*kids):
    print(("The youngest child is "+kids[2]))
my_function("Emil","Tobias","Linus")


def my_function(child3,child2,child1):
    print("The youngest child is "+child3)
my_function(child1="Emil",child2="Tobias",child3="Linus")

#**kwargs : If you don't know how many keywords will be passed into your function but it takes dictionaries as an input

def my_function(**kid):
    print("His last name is "+kid["lname"])
    
my_function(fname="Tobias",lname="Refsnes")

#%%

#Default parameter value 

def my_function(fname="Luis",lname="xyz"): #it prints Emil xyz
    print(fname+" "+lname)
my_function("Emil")


def my_function(country="Norway"):
    print("I am from "+country)
    
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#The value of country will be modified unless there is no value in the parenthesis. In that case, the one in the function is the default 
# !! YOU DON'T HAVE TO RETURN SOMETHING SOMETIMES YOU CAN JUST PRINT IN A FUNCTION


#%%

def largest(x,y):
    if(x>y):
        print(f"The largest number is {x}")
    else:
        if(x<y):
            print(f"The largest number is {y}")
        else:
            print("Both numbers are equal")
    
largest(1,4)
             
#%%

def largest(*list):
    max=0
    min=list[0]
    for i in range (len(list)):
        v=list[i]
        if v>max:
            max=v
        if v<min:
            min=v
            
    print(f"{max} is the largest value")
    print(f"{min} is the smallest value")

        
list=[]

for i in range(5):
    list.append(int(input("Give a number :")))
    
largest(*list)

#if you type in a string instead of an int, you get an error
#You have to handle the error 



#%%

a=5
b=0
try:
  print(a/b)

except: 
    print("Invalid values")
    

#Try except else finally : used to handle errors 
#try: test the block
#except: to handle the error 
#else : executes if no exception. Won't work if there's an error (not required)
#finally: code always executed. Will work even when there's an error (not required)


#There are specific types of errors like FileNotFoundError

#Except FileNotFound as e: print(e) ----> You give the error the name e and it calls it 

#%%

num=""
while(num=="" ):

 try:
  num=int(input("Enter a number :"))
 
 except ValueError as e: 
  print(e) #or you can put something else like a printed statement

 else:
    
  if(num%2)==0:
     print(f"{num} is even")
  else:
     print(f"{num} is odd")
     
     
#OR other way to do it : 

#%%

while True:
    try:
        num=int(input("Enter a number: "))
        if(num%2)==0:
           print(f"{num} is even")
          
        else:
           print(f"{num} is odd")
        break
        
    except ValueError as e:
           print(e)
            
     
#%%

num=""
while(num=="" or num<=0):
 try:
  num=int(input("Enter a number to find out if it's a prime number : "))
 
  if num<=0:
     print("number not valid")
 
 except TypeError as e :
    
    print(e)

        
 else:
    count=0
    for i in range (1,num+1):
        if num%i==0:
            count=count+1
            
    if count<=2:
        print(f"{num} is a prime number")

        
    







