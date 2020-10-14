

print("----------------------retrieving greater then numbers using normal program------------------------------")
listt=[1,2,3,4,5,6,7,8,9,10]
first_list=[]

def greater(listt):
    for i in listt:
        if i>6:
            first_list.append(i)
        else:
            pass
    return first_list
print(greater(listt))






print("\n\n\n\n-------------------------Usage of filter function-------------------------------------------------------")
a=[1,2,3,4,56,7,8,9,10]
def greater(i):
    return i>6
print(list(filter(greater,a)))

print("\n\n\n\n-----------------------filter function along with the lambda keyword------------------------------------")









a=[1,2,3,4,5]
summ=lambda num:num>2
print(list(filter(summ,a)))



print("\n\n\n\n---------------------------lambda in single line---------------------------------------------------------")
a=[1,2,3,4,5,6]
print(list(filter(lambda num:num>2,a)))
