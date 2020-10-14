# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:13:54 2020

@author: spandana
"""


num=1
sum=0
print("Enter the number for sum, press \"0\" to exit")

while num!=0:
    num=int(input("enter the number:"))
    sum=sum+num
    print("current Sum:",sum)
else:
    print("loop completed")