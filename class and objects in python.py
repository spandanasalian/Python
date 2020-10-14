# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:16:24 2020

@author: spandana
"""

#class declaration
class Student:
#note: double underscore __inint__
#init will call itself automatically when the object is called
    def __init__(self):
        self.name ="spandana"
        self.age  =20
        self.marks=95
       
        
#def indicates the declaration of the function
    def talk(self):
        print("name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)

#Si,object created
#init to initiolise the function
#init function cannot be called like the talk function
#that's why the object is created to call the function
        
#si.name means self.name
si = Student()
si.name="saniya"
print(si.name)
si.talk()

#if the object is not mentioned ,function would take the default value
s1=Student()
print(s1.name)