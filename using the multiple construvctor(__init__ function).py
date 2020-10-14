class Student:
    def __init__(sel):
        print('Hi')
        
#only the second constructor is taken into consideration
#two constructor or __init__ functions are not allowed
#self in th program is not mandatory,you can use any name
    def __init__(sel,n):
        sel.name=n
        print('Hellow')

    def display(sel):
        print("hi",sel.name)

si=Student("spandana")
si.display()