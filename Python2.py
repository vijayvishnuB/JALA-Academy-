#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=27
y=10
print(x+y)
print(x-y)
print(x*y)
print(x/y)


# In[2]:


x=27
x+=10
print(x)

y=37
y-=10
print(y)


# In[3]:


x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
if x==y:
  print("Both are equal")
else:
  print("Both are not equal")


# In[4]:


x=10
y=5
print(x<y)
print(x<=y)
print(x>y)
print(x>=y)


# In[5]:


a=(10,27,1,11)
print(max(a))
print(min(a))

