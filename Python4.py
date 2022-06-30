#!/usr/bin/env python
# coding: utf-8

# In[1]:


arr=[1,3,4,5,6];
sum=0;
for i in range(0,len(arr)):
    sum=sum+arr[i];
print("Sum of all the elements of an array:"+str(sum));


# In[2]:


def cal_average(num):
    sum=0
    for i in num:
        sum=sum+i
    avg=sum/len(num)
    return avg
print("The Average is ",cal_average([27,10,1,11,23]))


# In[3]:


arr=[1,3,4,5,1,2,6,3,8,6,9,7]
index=arr.index(3)
print("Index of 3: ",index)
index=arr.index(9)
print("Index of 9: ",index)
index=arr.index(8)
print("Index of 8: ",index)


# In[4]:


arr=[27,10,1,11,28]
for num in arr:
    if num==27:
        print("Element exist")


# In[5]:


arr=[45,56,79,84,33]
arr.remove(33)
print(arr)


# In[6]:


arr=['d','p','s','v']
arr1=[]
arr1=arr.copy()
print(arr1)


# In[7]:


arr=[222,40,500,645,888,990,1110]
arr.insert(2,1434)
print(arr)


# In[8]:


arr=[2222,576,5574,499,597,6327]
minposition=arr.index(min(arr))
print("The minimum is at position: ",minposition)
maxposition=arr.index(max(arr))
print("The maximum is at position: ",maxposition)


# In[9]:


arr=[4,11,10,6,1,27]
arr.reverse()
print(arr)


# In[10]:


arr=[10,27,11,1,27]
for i in range(0,len(arr)):
    for k in range(i+1,len(arr)):
        if arr[i]==arr[k]:
            print("Duplicate element in given array ",arr[k])


# In[11]:


arr=['d','p','s','v','m']
arr1=['d','l','p']
print("Common values in given arrays:",set(arr).intersection(arr1))


# In[12]:


arr=['d','p','s','v','m']
arr1=['d','l','p']
print("Common values in given arrays:",set(arr).intersection(arr1))


# In[13]:


arr=[101,201,301,401,501,601,701,801]
arr.sort()
print("The second largest number:",arr[-3])


# In[14]:


arr=[1,2,3,4,5,6,7,8,9]
evennumbers=0
oddnumbers=0
for i in arr:
    if i%2==0:
        evennumbers+=1
    else:
        oddnumbers+=1
print("Even numbers in given array:",evennumbers)
print("Odd numbers in given array:",oddnumbers)


# In[15]:


arr=[27,4,10,6,1,11]
arr.sort()
print("Difference of largest and smallest value:",arr[4]-arr[0])


# In[16]:


arr=[27,10,12,11,23,4,6]
for i in arr:
    if i==12:
        print("Exist in array")
    if i==23:
        print("Exist in array")

