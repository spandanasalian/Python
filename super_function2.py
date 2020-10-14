class Parent:
    def __init__(self,name):
        print("Parent __init__",name)
        
class Parent2:
    def __init__(self,name):
        print("Parent2 __init__",name)

#In case of multiple parent class the first declaration is taken
#into consideration
#super function return the first parent class
        
class Child(Parent,Parent2):
    def __init__(self):
        print("Child __init__")
        
#only one __init__ function is allowed 
#In case: Usage of two __init__ function
#result of the last init function is return
#To call the init function of Paren(First declared) class, bellow is the code
#class name followed by the function name followed by the arguments
        
        super().__init__("spandana")
#to print the second parent class
        Parent2.__init__(self,"spandana")

Child_obj=Child()
print(Child.__mro__)



#The super() builtin returns a proxy object that allows you to refer parent class 
#by 'super'.