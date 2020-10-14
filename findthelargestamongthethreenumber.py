num1=float(input("First Number:"))
num2=float(input("Second Number:"))
num3=float(input("Third Number:"))

if(num1>=num2) and (num1>num2):
    largest=num1
elif(num2>=num1) and (num2>num3):
    largest=num2
else:
    largest=num3
print("Largestnumber:",largest)