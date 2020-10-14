num1=int(input("Enter the number:"))
num2=int(input("Enter the second number:"))

def calculate(num1,num2):
    product=num1*num2
    if product<=1000:
        print(product)
    else:
        print(num1+num2)

calculate(num1,num2)