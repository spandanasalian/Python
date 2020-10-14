def merge_list(list_one,list_two):
    third_list=[]
    for num in list_one:
        if (num%2!=0):
            third_list.append(num)
    for num in list_two:
        if(num%2==0):
            third_list.append(num)
    return third_list

list_one=[10,20,24,25,27]
list_two=[13,43,24,56,12]
print("Result List:",merge_list(list_one,list_two))
            