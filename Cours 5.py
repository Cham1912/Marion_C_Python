#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:18:06 2023

@author: marion
"""
count=0
for i in range(4) :#i goes from 0 to 3
    count=count+i
    
print(count)

for i in range(2,4): #i goes from 2 to 3
    count=count+i
    
print(count)


ncount=0
n=10
for i in range(1,n+1,2) : #i goes from 1 to n with a step of 2
    ncount+=i
print(ncount)
    

    #%%
    
    #when making an addition, the initial value needs to be 0
    #when making a multiplication, the initial value needs to be 1 (or you'll multiply everything by 0)
    
for i in range(4):
   for j in range(3):
       print("i={},j={}".format(i,j))
       
       
       
#%%

n=int(input("What is the last value of the sum ? :"))

sum=0
for i in range(n+1) :
    sum+=i
    
print("The sum of all integers from 1 to {} is {}".format(n,sum))


#%%

n=int(input("What is the last value of the sum ? :"))

sum=0
for i in range (1,n+1):
    sum+=(i+1)/(i**2)
    
print(f"The result is :{sum: .2f}") # : .2f means you only get 2 decimal numbers. You can change the number 2 to any number

#%%

n=int(input("What number to you want to calculate the factorial of ? :"))
fact=1

for i in range (1,n+1) :
    fact=fact*i
    
print("The factorial {}! is equal to {}".format(n,fact))

#%%

n=10
for i in range(1,n):
    for j in range(1,n):
        
        print("{}{}".format(i,j))
    print("\n")
    
#%%

for i in range(1,10):
    for j in range(1,10) :
        if i!=j:
            print("{}{}".format(i,j))  #only prints the numbers where two digits don't repeat themselves like 22,33, ...
            
#%%

# triangular numbers formula : Ti=i(i+1)/2

a=int(input("Enter the number of triangular numbers you want :"))
for i in range(0,a+1):
 t=i*(i+1)/2

print(t)

#%%

for i in range(10):
    for j in range(10):
        for k in range(10):
            if i==j==k :
                print("{}{}{}".format(i,j,k))
                
                
#%%

for i in range(10):
    for j in range(10):
        for k in range(10):
            if i+j+k==22:
                print("{}{}{}".format(i,j,k))
                
#%%

for i in range(10):
    for j in range(10):
        for k in range(10):
            num=i*100+j*10+k
            if num==(i**3+k**3+j**3):
                print(num)
                
                
#%%

n=int(input("Which number do you want the positive divisors of ? :"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
        print("{} is a divisor of {}".format(i,n))
        
print(count)
        
#%%

n=int(input("Which fibonacci number to you want to go up to ? :"))

fib1=0
fib2=1
print(fib1)
print(fib2)

for i in range(2,n+1):
    fib3=fib2+fib1
    print(fib3)
    fib1=fib2
    fib2=fib3
    
    
                
         
  


        
        

