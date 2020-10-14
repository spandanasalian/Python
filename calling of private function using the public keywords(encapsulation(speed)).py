class Speed:
    def __init__(self):
        self.speed=10
        self.__speed_new=80

#double underescore to make the things private __speed_new
        
        
#general accessable public function     
    def display(self):
       return self.__speed_new
        
        
#speed can be made private,but still can be modified
#to solve this getters and setters are used
        
        
    def display1(self,new_name):
       self.__speed_new=new_name
        
si=Speed()
print(si.display())
si.speed=100
print(si.speed)
si.display1(120)

print(si.display())

#getter is the returning the value
#setter is modifying the value