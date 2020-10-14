class Polygon:
    
#below two lines are not mandatory
    
    _width=None
    _height=None
    
    def set_value(self,width,height):
        self._width=width
        self._height=height
        
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    
class Square(Polygon):
    def area(self):
        return self.get_width()*self.get_height()

class Triangle(Polygon):
    def area(self):
        return self.get_width()*self.get_height()*1//2
    
#Square
 
s1=Square()
s1.set_value(8,15)
print(s1.area())

#Triangle

s2=Triangle()
s2.set_value(8,15)
print(s2.area())