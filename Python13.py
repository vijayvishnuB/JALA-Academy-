#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Addition:
	# first sum for 2 params
	def my_sum(self, a, b):
		return a + b
	
	# second overloaded sum for 3 params
	def my_sum(self, a, b, c):
		return a + b + c
obj = Addition()
obj.my_sum(value1, value2)  # for first func
obj.my_sum(value1, value2, value3)  # for second func
print(obj.my_sum(3, 4))
print(obj.my_sum(3, 4, 5))

from multidispatch import dispatch  # importing the module

@dispatch(int, int)  # using the dispatch decorator to define two parameters as int
def mul(a, b):
    return a * b

@dispatch(int, int, int)  # defining 3 parameters as int
def mul(a, b, c):
    return a * b * c
	
@dispatch(float, float, float)  # defining 3 parameters as float
def mul(a, b, c):
    return a * b * c
print(mul(2.1, 3.4, 5.6))
print(mul(3, 4))
print(mul(2, 3, 4))

class MyClass:
    """"""

    #----------------------------------------------------------------------
    def _init_(self):
        """Constructor"""
    def my_method(self,parameter_A_that_Must_Be_String):
        print parameter_A_that_Must_Be_String

    def my_method(self,parameter_A_that_Must_Be_String,parameter_B_that_Must_Be_String):
        print parameter_A_that_Must_Be_String
        print parameter_B_that_Must_Be_String

    def my_method(self,parameter_A_that_Must_Be_String,parameter_A_that_Must_Be_Int):
        print parameter_A_that_Must_Be_String 

