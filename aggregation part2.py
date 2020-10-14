from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Square(Shape):
    def __init__(self,side):
        self._side=side
        
    def area(self):
        return self._side*self._side

Square_obj=Square(10)
print(Square_obj.area())