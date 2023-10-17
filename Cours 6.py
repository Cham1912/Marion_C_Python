#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 08:58:56 2023

@author: marion
"""
#Lists : store multiple values 
# also Tuples, Sets and dictionaries 

a=[1,2,3,4] #Syntax for a list 

b=["bon","jour"] #You can keep all types of values in a list 

c=[1,"bonjour"] #You can add different types in the same List 

us_president_list=['Joe Biden','Donald Trump','Barack Obama','Barack Obama','George W Bush','George W Bush']

a="Good Morning"
print(a[0])
print(us_president_list[3])

for president in us_president_list: #takes every value in the list and prints them in order 
    print(president) #instead of president, you can use anything as long as you use it after the for and in the print statement
    
# lists are mutable : You can modify them (add, remove or change items). You can't do that for sets and tuples

us_president_list.append('Bill Clinton') #Adds the specified element at the end of the list 

#%%

colors=['blue','red','green','pink','yellow','purple','grey']

for i in range(7):
    print(colors[i])
    
print("")


for color in colors:
    print(color)
    
    
print("")
    
colors.append('black')
colors.remove('grey')

for color in colors:
    print(color)
    
print("")
    
# remove only removes the first position where the element is encountered (if you delete barack obama, it'll only delete the first one)
    
colors[0]='white'

for color in colors:
    print(color)


#%%

#Tuples : start with () 
#Set : start with {}

#You use a list when you need to be able to modify things
#You use a tuple when you are keeping information that won't change (a list of presidents for example)

us_president_tuple=('Joe','Biden','2021-01-20','Democratic')

for i in us_president_tuple:
 print(i)

#%%

us_president_set={'Bill Clinton','Joe Biden','Donald Trump','Barack Obama','George W. Bush'}


#%%

import numpy as n

_Integer=[1,2,3,4]
print(_Integer)
smooth=[3.14,7,-2+3j,'water',False,[1,2],5,"Hello","Hi",7,n.e] #You can store a list inside another list
print(smooth)

print(smooth[5])
print(smooth[2:5]) #prints the elements in 2,3,4 th positions
print(smooth[:4]) #starts at 0 and ends at the 3rd position 
print(smooth[1:])

smooth[::2] #prints everything but only 1 value out of 2

#When using append, you cannot add multiple values at the same time, you have to add them one at a time
print("")
print(smooth[5][1]) #takes the list which is in 5th position and takes the element in position 1 in that list 

print(smooth[3][4])

print(smooth[1::2]) #starts at position 1 and step size 2


print(smooth[-4:-2]) #the last element is -1

#%%

chem_sim=["H","Pb","I","F","Cl","Ar","O"]
element=chem_sim.pop(2) #removes the item in 2nd position

print(chem_sim)

#%%


values=[1,2,3,4,5,6,7,8,9,10]
sum=0
n=int(input("Which value do you want the sum to stop at ?"))

for i in range(n):
    sum=sum+(1/values[i])
    
print(f"The sum from 1 to {n} is {sum:.2f}")

#%%

n=int(input("Enter a n value:"))
thelist=[]
for i in range(1,n+1):
    thelist.append(1/i)
Sn=sum(thelist) #Sum of all elements in the list

print("For n={} the sum accumulator is equal to {:.2f}".format(n,Sn)) #!!! How to write the format thing and round numbers

#%%

#Convert a string into a list

line="Temperature is 298.15 K before combustion"

words=line.split('i') #creates a new list where each element is the elements after the is 
print(words)

words2=line.split(" ")
print(words2)

#%%

line=input("Enter the desired temperature values")
smooth_txt=line.split()

print("List is now {}".format(smooth_txt))

temp=[]

for element in smooth_txt:
    value=float(element)
    temp.append(value)
    
print("The final list is {}".format(temp))

#%%

a=[1,3,5,7,11]
b=[13,17]
c=a+b
print("First instruction print:{}".format(c))
b[0]=-1
d=[]
for e in a:
    d.append(e+1)
print("Second instruction print:{}".format(d))
d.append(b[0]+1)
d.append(b[-1]+1)
print("Third instruction print : {}".format(d))
print("Fourth instruction print : {}".format(d[-2:]))
print("Fifth instruction print:{}".format(d[:-1]))
print("Sixth instruction print:{}".format(d[1:4]))

#%%

n=int(input("Enter a number :"))

list=[]

for i in range(1,n+1):
    list.append(i**2)
    
print(f"The squares of all numbers from 1 to {n} are {list}")

#%%

names=[]
grades=[]

n=int(input("How many students are there ? :"))

for i in range (n) :
    name=input("What is the name of the student ? :")
    names.append(name)
 
    grade=float(input("What is the grade of the student out of 10 ? :"))
    grades.append(grade)
 
print(" ")

for i in range (n):
        print("{:14} {:5.1f}".format(names[i],grades[i])) #{:14} means the names are left alignes
    
mean=sum(grades)/n
print("")
print("The mean is {}".format(mean))







    
    
