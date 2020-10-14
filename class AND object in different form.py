
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
        
si=Student("spandana","20","95")
si.display()