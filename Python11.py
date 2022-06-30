#!/usr/bin/env python
# coding: utf-8

# In[1]:


file1 = open("MyFile.txt","a")
file2 = open(r"D:\Text\MyFile2.txt","w+")

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

file1 = open("MyFile.txt","a")
data = file1.read()
print(data)
print()

import struct

thefile = open('somebinfile', 'r+b')
record_size = struct.calcsize(format_string)

thefile.seek(record_size * record_number)
buffer = thefile.read(record_size)
fields = list(struct.unpack(format_string, buffer))

# Perform computations, suitably modifying fields, then:

buffer = struct.pack(format_string, *fields)
thefile.seek(record_size * record_number)
thefile.write(buffer)

thefile.close(  )

f=open("GFG.txt","r")
f.seek(20)
print(f.tell())
print(f.readline())
f.close

>>> import os
>>> os.access('my_file', os.R_OK) # Check for read access
True
>>> os.access('my_file', os.W_OK) # Check for write access
True
>>> os.access('my_file', os.X_OK) # Check for execution access
False
>>> os.access('my_file', os.F_OK) # Check for existance of file

