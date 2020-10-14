def stringBalanceCheck(s1,s2):
    flag=True
    for char in s1:
        if char in s2:
            continue
        else:
            flag=False
    return flag

s1="th"
s2="Python"
flag=stringBalanceCheck(s1, s2)
print("S1 and s2 are balance",flag)

s1="tha"
s2="Python"
flag=stringBalanceCheck(s1, s2)
print("s1 and s2 are balanced",flag)