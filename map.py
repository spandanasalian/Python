lis=[1,2,3,4,5,6,7]
square_str=[]

def square(lis):
    for item in lis:
        square_str.append(item**2)
        
    return square_str
print(square(lis))

#indentation take into 

listt=[1,2,3,4,5,6,7,8]
def square(num):
    return num**2
print(list(map(square,listt)))
#list function to get the result in the form of list




listt=[1,2,3,4,5]
summ=lambda num:num**2
print(list(map(summ,listt)))


#--------------------------------single line programm(lambda)----------------------------------------------------
listt=[1,2,3,4,5,6,7,8,9]

print(list(map(lambda num:num**2,listt)))

