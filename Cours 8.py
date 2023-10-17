#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:12:00 2023

@author: marion
"""

#Dictionaries : List made of a key and a value that are associated together (the key is always the first and the value the second)

#Declare a dictionnary 
country_capitals={
    
   "United States" : "Washington D.C",
   "Italy" : "Rome",
   "England" : "London"
   
  } #curly braces

print(country_capitals)

#Dictionary keys must be immutable 
#There can't be lists in dictionaries because lists are mutable

#You can also use the function dict() to create a dictionary 

Dict=dict({1:'Geeks',2:'For',3:'Geeks'})
print(Dict)

#You can use the len() function to find the length of the dictionary 

print(len(country_capitals))

#You can have a dictionary in a dictionary 

Dict={1:"Geeks",2:"For",3:{'A':'Welcome','B':'To','C':'Geeks'}}

print(Dict[3]['A']) #print the first element in the sub-dictionary 
#You can't use indexes from 0 to n for dictionaries, you have the use the key 

Dict={'Dict1':{1:'Geeks'},'Dict2':{'Name':'For'}}

print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

#The dictionaries are actually mutable (haha funny joke)
#You can't change the keys, but you can change the values 

country_capitals["Italy"]="New Delhi" #Change a value in a dictionary using the key 
print(country_capitals)

country_capitals["Germany"]="Berlin" #Add a new value to a dictionary 
print(country_capitals)

del country_capitals["United States"] #delete an element
print(country_capitals)

country_capitals.pop("Italy") #other method with pop
print(country_capitals)

country_capitals.clear() #removes everything
print(country_capitals)

#PYTHON METHODS
#pop()
#update()
#clear()
#keys() : returns all dictionary keys
#values()
#get():returns the value of the specified key
#popitem(): removes the last inserted key and value as a tuple
#copy():returns a copy of the dictionary 

#see if a key is present in the dictionary 

my_list={1:'Hello','Hi':25,"Howdy":100}

print(1 in my_list) #says if the element is in the dictionary or not (boolean)
print("Howdy" not in my_list)
print("Hello" in my_list) #false because hello isn't an index, it's a value 


#dict.get(key, default="None") : If the key exists, it gives it to you. If it doesn't, will execute what's in the default 

#%%

country_capitals={
    
   "United States" : "Washington D.C",
   "Italy" : "Rome",
   "England" : "London"
   
  }

for country in country_capitals: #prints the keys 
    print(country)
print("\n")

for country in country_capitals: #prints the values
    capital=country_capitals[country]
    print(capital)
    
print("\n")


print(country_capitals.keys())
print(country_capitals.values())

#%%

#RECAP OF ALL THE METHODS 

dict1={1:"Python",2:"Java",3:"Ruby",4:"Scala"}

dict2=dict1.copy()
print(dict2) #copies a dictionary

dict1.clear()
print(dict1) #empties the dictionary

print(dict2.get(1)) #gets the value of the key in the parenthesis

print(dict2.items()) #gives all the items (key+value)

print(dict2.values()) #gives all the values

print(dict2.keys()) #gives all the keys

dict2.pop(4) #removes rhe item with the key in parentheses
print(dict2)

dict2.popitem() #removes the last item
print(dict2)

dict2.update({3:"Scala"}) #modifies the dictionary 
print(dict2)

#%%

#PYTHON COLLECTIONS 

#Lists : Ordered, changeable, allows duplicate members (for matrixes for example)
#Tuple : Orderes, unchangeable, allows duplicate members
#Set : unordered, unchangeable, unindexed, no duplicate members
#Dictionary : Ordered, changeable, no duplicate members

#%%

cities=('Paris','Athens','Madrid')
continent=('Europe')
dictionary=dict.fromkeys((cities,continent)) #turns a tuple into a dictionary. The key has to be a str, num or tuple
print(dictionary)

dict2=dict.fromkeys(cities)
print(dict2)

countries=('France','Greece','Spain')

dict3=dict(zip(cities,countries))
print(dict3)

#%%

keys=['Ten','Twenty','Thirty']
values=[10,20,30]

dict1=dict(zip(keys,values)) #assigns each value to the corresponding one 
print(dict1)

#%%

dict1={"Ten":10,"Twenty":20,"Thirty":30}
dict2={"Thirty":30,"Fourty":40,"Fifty":50}

dict1.update(dict2)
print(dict1)

#OR

dict3={**dict1,**dict2}
print(dict3)

#%%

sampleDict={"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
            
print(sampleDict['class']['student']['marks']['history'])

#%%

employees=["Kelly","Emma"]
defaults={"designation":"Developer","Salary":800}

dict1=dict.fromkeys(employees,defaults)
print(dict1)

print(dict1['Kelly'])
    
#%%

sample_dict={"name":"Kelly","age":25,"salary":8000,"city":"New york"}

sample_dict.pop("name")
sample_dict.pop("salary")
print(sample_dict)


#%%

sample_dict={'emp1':{'name':'John','salary':7500},'emp2':{'name':'Brad','salary':'500'}}
print(sample_dict)
sample_dict.update({'emp2':{'salary':8500}})
print(sample_dict)





