num=[10,20,30,40,50,60,70]
def check_list(num):
    firstElement=num[0]
    lastElement=num[-1]
    
    if(firstElement==lastElement):
        return True
    else:
        return False
    
print("Return is",check_list(num))
