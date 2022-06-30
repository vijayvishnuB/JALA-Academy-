#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Python:
#Access through class    
  staticVariable = 27
print(Python.staticVariable)


# In[2]:


#Change within an class
Python.staticVariable = 10
print(Python.staticVariable)


# In[3]:


#Access through an instance
instance = Python()
print(instance.staticVariable) 


# In[4]:


#Change within an instance
instance.staticVariable = 1
print(instance.staticVariable)
print(Python.staticVariable)

