result=None
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

try:
    result=a/b
    
except Exception as e:
    print("error in the code")
    print(type(e))

print("-----------------------print------------------------")
print(result)