#!/usr/bin/env python
# coding: utf-8

# In[1]:


string1='Hello'
string2="Beautiful"
string3='''Amazing'''
string4="""Cute"""
print(string1)
print(string2)
print(string3)
print(string4)


# In[2]:


str1="Amazing"
str2="World"
print("String 1: ",str1)
print("String 2: ",str2)
str=str1 + str2
print("Concatenated two different strings: ",str)


# In[3]:


str="Dhivaagar"
print(len(str))


# In[4]:


myString="concentration"
print(myString[3 : -1])
print(myString[5 : ])
print(myString[ : 4])
print(myString[:])


# In[5]:


str3='sangeeth'
str1='gee'
str2='h'
print("Position of gee: ",str3.index(str1))
print("Position of h: ",str3.index(str2))


# In[8]:


import re

pattern='^a...s$'
string='abaas'
result=re.match(pattern,string)

if result:
  print("Matched")
else:
  print("Not Matched")


# In[6]:


str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
if str1==str2:
    print("first and second strings are equal and same")
else:
    print("first and second strings are not same")


# In[7]:


string='vijay vishnu'
print(string.startswith('vijay'))
print(string.endswith('vishnu'))
print()


# In[9]:


greeting="      Hi   "
print(greeting.strip(),"I am Dharanis")


# In[10]:


text='brass'
replaced_text=text.replace('b','g')
print(replaced_text)


# In[11]:


str='hi-dinesh-how are you?'
print(str.split("-"))
print()


# In[12]:


name1,name2,name3=input("Enter 3 names:").split()
print("Name 1:",name1)
print("Name 2:",name2)
print("Name 3:",name3)


# In[15]:


num=27
value=num.__str__()
print('Value: ',value)
print('Type: ',type(value))


# In[16]:


str='amazing'
str1='WORLD'
print(str.upper())
print(str1.lower())

