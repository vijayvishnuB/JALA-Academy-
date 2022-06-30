#!/usr/bin/env python
# coding: utf-8

# In[1]:


class A():  
    def display(dp):
        print("Display Inside class A ")
 # class A show method    
    def show(self):
        print("Show Inside class A")


# In[2]:


class B (A): 
    def print(pt):
        print("Print Inside class B")    
    # class B show method
    def show(self):
        print("Show Inside class B")


# In[3]:


class C (B): 
          
    # class C show method
    def show(self):
        print("Show Inside class C ")  


# In[4]:


# Driver code 
s = A()
s.display()
k= B()
k.print()
g = C()   
g.show()

