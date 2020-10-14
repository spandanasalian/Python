class Parent:
    def __init__(self,name):
        print("Parent __init__",name)
        
class Child:
    def __init__(self):
        print("Child __init__")
        
#only one __init__ function is allowed 
#In case: Usage of two __init__ function
#result of the last init function is return
#To call the init function of Paren(First declared) class, bellow is the code
#class name followed by the function name followed by the arguments
        
        Parent.__init__(self,"spandana")

Child_obj=Child()