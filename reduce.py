a=[1,2,3,4,5,6,7,8,9,10]
x=0

def sum(a):
    global x
    for num in a:
        x+=num
    return x
print(sum(a))

from functools import reduce



print("\n\n\n\n----------------------------------reduce function and lambda keyword--------------------------------------")

a=[1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y:x+y,a))