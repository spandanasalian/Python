num=int(input("Enter a number:"))
def print_factors(num):
    factor_list=[]
    for i in range(1,num+1):
        if num %i==0:
            factor_list.append(i)
    return factor_list
factors=print_factors(num)
print("Factors are:",factors)