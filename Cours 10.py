#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:32:14 2023

@author: marion
"""
#%%

#NumPy Library 

#NumPy is mostly used in statistical analysis

import numpy as np

#The processing time of lists is slower than numpy 
#Numpy stores the number in 4 bytes (32 bits) but you can change it 

#You can't multiply lists but you can multiply them if you create them with numpy 


a=np.array([1,2,3],dtype='int32') #to create your array 
print(a)

b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]]) #to create a 2d array 
print(b)

print(a.ndim) #gives the dimension of the array 
print(b.ndim)


print(b.shape) #gives the shape of the array(height,length)
print(a.dtype) #gives the type of the values in the array 

print(a.itemsize)
print(a.size)

#%%

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a[1,5])
print(a[1,-3]) #reminder : the last item is the -1 so the -3 is the 2nd to last 
print(a[0:])

print(a[:,2]) #gives the 3rd item of both rows
print(a[-1:]) #gives the entire 2nd row 

# it's [row,column)]

print(a[0,1:-1:2]) #line 0, from index 1 to the last, with a step of 2

print(a[0,::2])

print(np.zeros((2,3))) #make a matrix of zeros

print(np.full((2,2),(99)))

print(np.full_like(a,4))
print(np.random.rand(4,2))
print(np.random.randint(-4,8,size=(3,3)))


arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)


print(np.array([[1,0,1],[1,2,1],[1,0,1]]))
#or
print("\n")

arr2=np.array([[1,0,1]])
print(arr2)

r1=np.repeat(arr2,3,axis=0)
print(r1)
print("\n")

r1[1,1]=2
print(r1)

#%%

output=np.ones((5,5))
print(output)

z=np.zeros((3,3))
z[1,1]=9
print(z)

output[1:-1,1:-1]=z
print(output)

#%%

a=np.array([1,2,3])
b=a
b[0]=100
print(b)
print(a) #if b is a copy of a, then if you modify b, you also modify a 

print(np.matmul(a,b))

#%%

stats=np.array([[1,2,3],[4,5,6]])
print(np.min(stats))
print(np.min(stats,axis=0))

#%%

import numpy
npoints=21
values=numpy.linspace(-2.0,2.0,npoints) #gives 21 points dividing the interval 
print(values)

#%%

import numpy
vect=numpy.arange(9)
print(vect)


