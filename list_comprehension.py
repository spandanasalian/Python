lst=[1,2,3,4,5,6,7,8]
sq_lst=[]

for num in lst:
    sq_lst.append(num**2)
print(sq_lst)



lst=[1,2,3,4,5,6,7,8,9,10]
sq_list=[num**2 for num in lst]
print(sq_list)


lst=[1,2,3,4,5,6,7]
sq_lst=[]

for num in lst:
    if num>3:
        sq_lst.append(num**2)
print(sq_lst)

#------------------if statement ater the iteration------------------------------------------------------------------------
lst=[1,2,3,4,5,6,7,8,9,10]
sq_list=[num**2 for num in lst if num>3]
print(sq_list)







lst=[1,2,3,4,5,6,7]
sq_lst=[]

for num in lst:
    if num>3 and num%5==0:
        sq_lst.append(num**2)
print(sq_lst)

#------------------if statement ater the iteration------------------------------------------------------------------------
lst=[1,2,3,4,5,6,7,8,9,10]
sq_list=[num**2 for num in lst if num>3 and num%5==0]
print(sq_list)



sq_list=[num**2 for num in range(1,101) if num>3 and num%5==0]
print(sq_list)


