#!/usr/bin/env python
# coding: utf-8

# In[1]:


name=input("Enter your name:")
print(name)


# In[2]:


#This is a singleline comment
print("She is beautiful")

#This is a 
#multipleline comment
print("He is so cute")


# In[4]:


x=27
print(type(x))

y=27.4
print(type(y))

a=True
print(type(a))

b="Dharani"
print(type(b))


# In[5]:


a=27
def variable():
  print("Inside function",a)

variable()
print("Outside function",a)


def variable(): 

  #local variable
  a='Internship'
  print(a)

variable()

