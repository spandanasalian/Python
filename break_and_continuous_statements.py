# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:20:39 2020

@author: spandana
"""


#break statement is used to get out from the loop

a=[0,1,2,3,4,5,6,7]
for x in a:
    if x==2:
        break
    print(x)
    
i=0
while i<5:
    if i==3:
        break
    print(i)
    i+=1