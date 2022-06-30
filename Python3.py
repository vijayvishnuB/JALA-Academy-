#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(10):
    print("Bright IT Career")


# In[2]:


i=1
while(i<=10):
    print(i)
    i+=1


# In[3]:


a=5
b=5
if(a==b):
    print("a is equal to b")
else:
    print("a is not equal to b")


# In[4]:


num=int(input("Enter any number:"))
if(num%2)==0:
    print("The number is even")
else:
    print("The number is odd")


# In[5]:


a=10
b=20
print("even numbers between 10 to 20: ",end=" ")
while a<=b:
    if(a%2==0):
        print("{0}".format(a),end=" ")
    a=a+1
print()


# In[6]:


a=1
print("Print numbers from 1 to 10: ",end=" ")
while True:
    print(a,end=" ")
    a=a+1
    if(a>10):
        break
print()


# In[7]:


num=int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")


# In[11]:


num=int(input("Enter a number: "))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
if flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")


# In[9]:


num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome")
else:
    print("Not a palindrome")


# In[13]:


num=int(input("Enter a number:"))
if num % 2==0:
    print("{0} is Even".format(a))
else:
    print("{0} is Odd".format(a))


# In[16]:


def get_gender(self):
    if self.use_url==none:
        print("i am anonymous use.")
        return'unknown'
    else:
        if self.soup==none:
            self.parser()
            soup=self.soup
            try:
                gender=str(soup.find("span",class_="itemgender").i)
                if(gender=='<iclass="icon icon-profile-female"></i>'):
                    return'female'
                else:
                    return'male'
            except:
                return'unknown'

