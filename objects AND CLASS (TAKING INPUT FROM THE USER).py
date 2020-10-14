n=input("Enter your name:")
m=int(input("Enter your age:"))
a=int(input("Enter the marks:"))

class Student:
#n,m,a are the positional arguments
    def __init__(self,n,m,a):
        self.name=n
        self.age=m
        self.marks=a
    
    def display(self):
        print("your name is:", self.name)
        print('Your age is :',self.age)
        print("Your marks is:",self.marks)
        
si=Student(n,m,a)
si.display()