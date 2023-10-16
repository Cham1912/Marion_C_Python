#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:10:57 2023

@author: marion
"""

import matplotlib.pyplot as plt

import numpy as np 

x=np.linspace(-2,2,101)
y=x**2
print(x)

plt.plot(x,y) # creates the plot 
plt.title("Graph of x^2 vs x") #gives a title to the plot
plt.show()

#when using a notebook you have to add %matplotlib inline for it to show the graphs but in spyder you see
#the graphs in plots

#%%

x=np.linspace(0,3*np.pi,500)
plt.plot(x,np.sin(x**2))
plt.title('A simple chirp')

plt.plot(y) #if you only plot one coodinate, it takes the number of points as the x 

#%%

x=np.linspace(-2,2,101)
y=x**2

plt.xlabel("x")
plt.ylabel("f(x)")

plt.xlim(-1.5,1.5)
plt.ylim(-0.5,2.5)
plt.title("Chart Title")
plt.plot(x,y)
plt.show()

#%%
#plots 2 lines<

x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("y")
y=x**2
plt.plot(x,y,label="x^2")
y2=x**4
plt.plot(x,y2,label="x^4")
plt.legend()
plt.show()

#%%

x=np.linspace(-2,2,11)
plt.xlabel("x")
plt.ylabel("f(x)")

plt.plot(x,y2,'g',label="x**2")
plt.plot(x,y3,'ro',label="x**3")
plt.plot(x,y4,'b',label="x**4")

#%%

x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y=x**2
plt.plot(x,y,label="x**2")
y2=x**4
plt.plot(x,y2,label="x**2")
y2=x**4
plt.plot(x,y2,label="x**4")
plt.savefig("fig1.png")
plt.show()

#%%

#Exercice

import numpy as np

n=int(input("How many points need to be drawn ? :"))
x=np.linspace(-1,1,n)
u=2*np.pi*x
y=np.cos(u)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("2pix")
plt.plot(x,y)
plt.savefig("figexo1.png")
plt.show()

#%%

import numpy as np

n=int(input("How many points need to be drawn ? :"))
x=np.linspace(-1,1,n)
v=np.sin(np.pi*2*x)
y=np.cos(2*np.pi*x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("2pix")
plt.plot(x,y,label="cos function")
plt.plot(x,v,label="sin function")
plt.savefig("figexo1.png")
plt.legend()
plt.show()

#%%
n=""
while(n==""):
 import numpy as np
 try:
  n=int(input("How many points need to be drawn ? :"))
 
 except ValueError as e:
    print(e)

else:
 x=np.linspace(0,4,n)

 y=np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
 plt.plot(x,y)

#%%

n=int(input("How many points need to be drawn ? :"))
T=int(input("What is the temperature of the gaz ?:"))
plt.xlabel("Vm (L/mol)")
plt.ylabel("pressure (atm)")
plt.title("Isotherm (ideal gaz)")
V=np.linspace(2,10,n)
p=((0.08206)*T)/V
plt.savefig("isotherm.jpg")

plt.plot(V,p)

#%%

n=int(input("How many points need to be drawn ? :"))
nT=int(input("How many different temperatures do you want ?:"))

for i in range (nT):

 T=int(input("What is the temperature of the gaz ?:"))
 plt.xlabel("Vm (L/mol)")
 plt.ylabel("pressure (atm)")
 plt.title("Isotherm (ideal gaz)")
 V=np.linspace(2,10,n)
 p=((0.08206)*T)/V
 plt.savefig("isotherm.jpg")

 plt.plot(V,p)


#%%

n=int(input("How many points need to be drawn ? :"))
i=int(input("What is the start value of the interval ?:"))
j=int(input("What is the end value of the interval ? :"))
xo=int(input("What is the value of x0 ? :"))
s=float(input("What is the value of s ?"))

x=np.linspace(i,j,n)
y=(1/np.sqrt(2*np.pi))*np.exp((-1/2)*((x-xo)**2)/s**2)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.title("Gaussian Function")


#%%
n=int(input("How many points need to be drawn ? :"))
x=np.linspace(0,3,n)

y=np.exp(-x)
w=np.sin(3*np.pi*x)*np.exp(-x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Functions")

plt.plot(x,y,label="e-x")
plt.plot(x,w,label="sin(3*pi*x)*e-x")
plt.legend()


#%%

n=int(input("How many points need to be drawn ? :"))
i=int(input("What is the start value of the interval ?:"))
j=int(input("What is the end value of the interval ? :"))
p=int(input("How many functions need to be represented ? :"))

for a in range(p):

 xo=int(input("What is the value of x0 ? :"))
 s=float(input("What is the value of s ?"))

 x=np.linspace(i,j,n)
 y=(1/np.sqrt(2*np.pi))*np.exp((-1/2)*((x-xo)**2)/s**2)
 plt.xlabel("x")
 plt.ylabel("f(x)")
 plt.plot(x,y,label="xo={:.1f},s={:.1f}".format(xo,s))
 plt.title("Gaussian Function")

plt.legend()





