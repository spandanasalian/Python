i=[]
for num in range(2000,3201):
    if num%7==0 and num%5!=0:
        i.append(str(num))
        
print(i)
print(','.join(i))

# l = []

# for num in range(2000, 3201):
#    if num%7==0 and num%5!=0:
#        l.append(str(num))

# #printing all numbers in list sequence
# print(l) 

# #printing comma-separated sequence
# print(','.join(l)) 