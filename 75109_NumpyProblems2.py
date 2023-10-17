#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:55:34 2023

@author: marion
"""

import numpy as np

#%%

#Write a NumPy program to create a vector with values from 0 to 20 
#and change the sign of the numbers in the range from 9 to 15.


a=np.linspace(0,20,21)
print(a)

for i in range (9,16):
    a[i]=-a[i]
    
print(a)

#%%

#Write a NumPy program to create a vector with values ranging from 15 to 55 
# and print all values except the first and last.


a=np.linspace(15,55,41)

for i in range (1,40):
    print(a[i],end=" ") #prints everything in one line
    

#%%

#Write a NumPy program to create a 3X4 array and iterate over it.

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

for element in a :
    print(element)
    

#%%

#Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.

a=np.linspace(5,50,10)
print(a)

#%%

#Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.

a=np.random.randint(0,11,size=(1,5))
print(a)


#%%

#Write a NumPy program to multiply the values of two given vectors.

a=np.array([1,2,3])
b=np.array([10,20,30])

for i in range(3):
    a[i]=a[i]*b[i]
    
print(a)

#%%

#Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

a=np.arange(10,22).reshape(3,4)
print(a)


#%%

#Write a NumPy program to find the number of rows and columns in a given matrix.

a=np.array([[1,2],[3,4],[4,5]])
rows,columns=a.shape #shape gives the amount of rows and columns
print(rows)
print(columns)

#%%

#Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.

a=np.ones((4,4))

for i in range(4):
    for j in range(4):
        if i==j:
            a[i][j]=0
            
print(a)

#%%

#Write a NumPy program to find common values between two arrays.

a=np.array([0,10,20,40,60])
b=np.array([10,30,40])
c=np.array([])

for i in range(5):
    for j in range(3):
        if a[i]==b[j]:
            c=np.append(c,a[i])
            
print(c)
    
#%%

#Write a NumPy program to get the unique elements of an array.

def unique_elements(a):
    u_e=np.unique(a) #np.unique gives the unique values in the table a 
    return u_e         
 

a=np.array([10,10,20,20,30])
b=np.array([[1,1],[2,3]])

print(unique_elements(a))
print(unique_elements(b))


#%%

#Write a NumPy program to compute the cross product of two given vectors.

a=np.array([1,2,3])
b=np.array([4,5,6])

c=np.cross(a,b) #Cross is a numpy function that calculates the cross products automatically
print(c)


#%%

#Write a NumPy program to convert cartesian coordinates to polar coordinates 
#of a random 10x2 matrix representing cartesian coordinates.

a=np.random.rand(10,2)

x=a[:,0] #takes the first column of a 
y=a[:,1] #takes the second column of a

r=np.sqrt(x**2+y**2)
t=np.arctan2(y,x)

print("x :",x)
print("y :",y)
print("r :",r)
print("theta :",t)

#%%

#Write a NumPy program to find the closest value (to a given scalar) in an array.

a=np.linspace(0,99,100)

b=34.99062268928913

print(np.argmin(np.abs(a-b))) #argmin gives the smallest value among all the ones calculates with abs(a-b)










