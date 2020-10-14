

#class declaration
class Student:
#note: double underscore __inint__
#init will call itself automatically when the object is called
#init is the contructor method
#self is the parameter in the def __init__(self)
    
#__init__ (constructor):constructor is the spacial method used to initialize
#the instance(object) variable of the class
    def __init__(self):
        self.name ="spandana"
        self.age  =20
        self.marks=95
#print the init function
        print('__init__')
       
        
#def indicates the declaration of the function
    def talk(self):
        print("name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
#self contains the memory location

#Si,object created
#init to initiolise the function
#init function cannot be called like the talk function
#that's why the object is created to call the function
        
#Student(), parameter is hidden nothing but the self 
#so we can call add the object si or any other
si = Student()



#if the object is not mentioned ,function would take the default value
s1=Student()
print(id(si))
print(id(s1))