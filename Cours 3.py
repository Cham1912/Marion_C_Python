#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:15:34 2023

@author: marion
"""

message="Good Morning"
print(len(message)) #prints the length of the string (the space between the words counts as a character)

print(message[8]) #prints the letter in the 8th position. THE FIRST INDEX IS 0 NOT 1
print(message[0])

print(message[0:4]) #prints all the characters from the starting point to the ending point
# the ending point is excluded to you have to increase by 1 if you want to include it 
    
print(message[8:12])
print(message[8:]) # if you want to go all the way to the end you can not add an ending index. 

print(message[-1]) # shows the last character of the string (you can do -2,-3, ....)

#%%

# print in upper case : 
print(message)
print(message.upper())
print(message.lower())

print(message.count('o')) #shows how many times the character in parenthesis appears in the string

print(message.find('o')) #shows the index of the character (only the first one)


new=message.replace('Morning','Afternoon') #takes the string message and replaces the part before the coma with the one after
print(new) # ! you have to keep the new string in a new variable, the original one wasn't modified


print(dir(str)) #shows all the possible attributes that you can use one strings 

print(message.count('ing')) #shows how many times you get the letter/string in the parenthesis

#%%

#loops 

#1: if loop :
    
num=int(input("Enter a number"))
if num>5 :
   print("Youhou")
else:
    print("cafetière")
    
#%%    
#even or odd number 
num=int(input("Enter a number"))
if num%2==0 :
    print("The number {} is even".format(num))
else:
    print("The number {} is odd".format(num))
    
#you can also do : print(f"The number {num} is even")

print(f"Le chiffre {num}")

#%%
#if you have more than two conditions : elif

#if condition1:
#    Action_1
#elif condition2:
#    Action_2
#elif condition3:
#   Action_3
#else:
#   Action_n


weight=float(input('Enter your weight'))
    
height=input('Enter your height')
if height[-2]=='c':
 height=float(height[0:-3])*0.1
 print(f"your height in meters is : {height}")
if height[-1]!='m':
    height=float(height)
else :
    height=float(height[0:-3])

bmi=weight/(height**2)

if bmi<18.5 :
    print("Underweight")
    
elif bmi>=18.5 and bmi<25:
        print("Normal")
elif bmi>=25 and bmi<30:
        print("Overweight")
else:
        print("Obesity")
        
        
        
#the and operator is the word and 

#%%

num1=int(input("Enter a number"))
num2=int(input("Enter another number"))

if(num1<num2):
    print("{} isn't divisible by {} because it is smaller ".format(num1,num2))
    
elif num1%num2==0:
    result=num1/num2
    print("{} is divisible by {} and the result is {}".format(num1,num2,result))
    
else:
    result=num1/num2
    remainder=num1%num2
    print("{} is not divisible by {}. The result is {} and the remainder is {}".format(num1,num2,result,remainder))


#%%

num1=int(input("Enter a number"))
num2=int(input("Enter another number"))

if num1>2 :
    print(f"{num2} is the minimum")
    
else :
    print(f"{num1} is the minimum")
    
#%%

units=int(input("Enter the amount of units : "))

if units<=100 :
    print("No charge")
    
elif units>100 and units<=200:
    charge=(units-100)*5
    print(f"Your total is {charge} euros")
    
else :
    charge=(100*5)+(units-200)*10
    print(f"Your total is {charge} euros")







