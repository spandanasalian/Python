class Example:
    def __init__(self):
        self.x=10
        self._y=20
        self.z=40
        
    def public_method(self):
        print(self.x)
        print(self._y)
        print(self.z)
        self.__private_method()
#private methods cannot be accessed (double underscore)      
    def __private_method(self):
        print("inside private method")
        
E=Example()
E.public_method()
#E.__private_method()

