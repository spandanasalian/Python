# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 19:46:50 2020

@author: spandana
"""


i=int(input("Enter your age:"))
if i>0:
    print("Positive")
    if i%2==0:
        print("even")
    else:
        print("odd")
else:
    print("Negative")