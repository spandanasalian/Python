for i in range(5,81):
    print(i)
    
num=range(5,81)
print(list(num))

for i in range(0,30,3):
    print(i)
    
a = ["1", 1, "1", 2]
print(set(a))

name={"a":1,"b":2,"c":3}
a=name.values()
print(sum(a))


name={"a":1,"b":2,"c":3}
name=dict((key,value) for key,value in name.items() if value<=1)

print(name)


