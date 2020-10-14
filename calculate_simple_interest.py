p=float(input("Enter the principal amount-"))
t=float(input("Enter the time period-"))
r=float(input("Enter rate of interest-"))

def simple_interest(p,t,r):
    si=(p*t*r)/100
    print("Simple Interest is",si)

simple_interest(p,t,r)