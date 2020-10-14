
class Student:
#n,m,a are the positional arguments
    def __init__(self,n,m,**a):
        self.name=n
        self.age=m
        self.marks=a
        
    
    def display(self):
        print("your name is:", self.name)
        print('Your age is :',self.age)
        print("Your marks is:",self.marks)
        
#didn't passed the marks 
#didn't passed the marks 
# that takes the default arguments
#to display only the value,form is tuple
#to display the key,values :dictionary
si=Student("spandana",20,science=69,maths=70,physics=89,chemistry=95)
si.display()
print("----------------------------------------------------------")
si=Student("saniya",20,science=69,maths=70,physics=89,chemistry=95)
si.display()