#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 03:36:36 2023

@author: marion
"""

#Ex 1

for i in range(66):
    print("-",end="")
    i+=i
    
print("Finding the state of an element with its temperature :")
    
print("\n")

Elements={'H':[1,14,20,'Hydrogen'],'He':[2,1,4,'Helium'],'Li':[3,453,1603,'Lithium'],'Be':[4,1560,2742,'Beryllium'],'B':[5,2349,4200,'Boron'],'C':[6,3915,3915,'Carbon'],'N':[7,63,77,'Nitrogen'],'O':[8,54,90,'Oxygen'],'F':[9,53,85,'Fluorine'],'Ne':[10,25,27,'Neon']}

print(Elements.keys())
E=input("Which element do you want to find the state of ? :")
T=float(input("What is the temperature ?:"))

if Elements[E][1]>=T:
    print(f"The {Elements[E][3]} is in liquid form")
elif Elements[E][2]<=T:
    print(f"The {Elements[E][3]} is in gas form")
    
else:
    print(f"The {Elements[E][3]} is in a solid form")
    

print("\n")
for i in range(66):
    print("-",end="")
    i+=i
print("\n")
    

#%%

banks={'ANZ':[2.3,4.1],'Bank of Australia':[0.1,5],'Commonwealth Bank':[3.5,3.8],'Westpac':[3.7,3.7]}
print(banks.keys())

m=float(input("How much is the mortgage ? :"))
y=int(input("How many years will the mortgage last ? :"))
b=input("Which bank provides your mortgage ? :")


if y<=2:
    re=y*m*(banks[b][0])/100
    print(re)
    
else:
    re=2*y*m*(banks[b][0])/100+(y-2)*m*(banks[b][1])/100
    print(re)

