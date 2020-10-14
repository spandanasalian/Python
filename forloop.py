# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:23:13 2020

@author: spandana
"""


A=[1,2,3,4,5,6]
B=(1,2,3,4,5,6)
C={1,2,3,4,5,6}
D="spandana"
E={"name":'spandana',"age":19}
for i in A:
    print(i)
for i in E:
    print(i)
for i in E.values():
    print(i)
for i in E.keys():
    print(i)
for x,y in E.items():
    print(x,"",y)
#for x,y in E.items():
    #print(x+""+y)