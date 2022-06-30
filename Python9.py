#!/usr/bin/env python
# coding: utf-8

# In[1]:


from abc import ABC, abstractmethod
 
class Polygon(ABC): #base class / super class
 
    @abstractmethod
    def noofsides(self):
        pass
class Triangle(Polygon): #subclass
 
    # overriding abstract method
    def noofsides(self):
        print("Triangle: I have 3 sides")
 
class Pentagon(Polygon): #subclass
 
    # overriding abstract method
    def noofsides(self):
        print("Pentagon: I have 5 sides")
 
class Hexagon(Polygon): #subclass
 
    # overriding abstract method
    def noofsides(self):
        print("Hexagon: I have 6 sides")
R = Triangle()
R.noofsides()
R = Pentagon()
R.noofsides()
 
K = Hexagon()
K.noofsides()

