#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 08:25:42 2023

@author: marion
"""

# when declaring a variable, the first character cannot be a number 
#4my_name='Marion' creates an error

#you have to declare your variable in small letters 
#declare variables with things that are easy to understand (num or number instead of n)

R=1
n=2
T=3
V=4
p=n*R*T/V

#to write the result, you can do : 
    
print("At temperature {} K the pressure is {} atm.".format(T,p))
# You can put the accolades where you want to add variables and type .format(1st thing, 2nd thing, ...)


a=2
b=3
area=a*b
print("The area of the edge rectangle {} and {} is valid {}.".format(a,b,area))

# operator // : 7//10 for example gives 0 instead of 0.7 

a=5
b=3
c=2.5

d=(2*a+b**2)/c
print("The answer is {}".format(d))


V=input("Enter volume in L:")
V=float(V)
p=n*R*T/V

print("Gaz pressure is {} atm".format(p))

#typecasting : when you want a variable to be a certain type :
    


r=float(input("Enter the rayon :"))
h=float(input("Enter the height :"))
V=float((1/3)*3.14*r**2*h)
print(V)

#import modules on Python : import + name of the module

import math as m # you can import the module with a name so that its shorter 
print(m.pi)

# if you haven't installed the modules, you have to install them in your ide

import pandas
import matplotlib
import random
import sys
#import cclib
import numpy


# start with the math module : 
    
dir(m)
print(m.cos(0))


num1=float(input("Enter a numeric value :"))
num2=float(input("Enter another numeric value :"))
sum=num1+num2
product=num1*num2
print("The sum of {} and {} is {}".format(num1,num2,sum))
print("The product of {} and {} is {}" .format(num1,num2,product))

#%%
temp=float(input("Enter your temperature in Celcius : "))
kelvin=float(temp+273.15)
print("The temperature in Kelvin is {}".format(kelvin))

#%%
l=int(input("What is the lenght of the sides of the cube ?"))
area=6*l**2
vol=l**3

print("The area of the cube is {}".format(area))
print("The volume of the cube is {}".format(vol))

#%%

num10=int(input("How many 10 euro banknotes do you have ?"))
num20=int(input("How many 20 euro banknotes do you have ?"))
num50=int(input("How many 50 euro banknotes do you have ?"))

sum=num10*10+num20*20+num50*50
print("You have {} euros in total".format(sum))

#%%
import math as m
rad=float(input("What is the radius of the circle ?"))
l=2*m.pi*rad
a=m.pi*rad**2
print("The length of the circle is {} cm and the area of the circle is {} cm^2".format(l,a))

#%%

import math as m 
rad=float(input("What is the radius of the sphere ?"))
a=4*m.pi*rad**2
v=(4/3)*m.pi*rad**3
print("The area of the sphere is {} and the volume of the sphere is {}".format(a,v))

#%%

a=float(input("What is the value of A ?"))
ea=float(input("What is the value of Ea ?"))
r=8.3144621
t=float(input("What is the value of T ?"))

k=a*m.exp(-ea/r*t)

print("The value of k is {} s^-1".format(k))


#%%

s1=int(input("Length of the 1st side of the triangle in cm"))
s2=int(input("Length of the 2nd side of the triangle in cm"))
an=int(input("Angle between the sides of the triangle in degrees"))

an=m.radians(an)

s3=m.sqrt(a**2+b**2-2*a*b*m.cos(an))

print("The third side of the triangle measures {} cm".format(s3))




    




    

    
