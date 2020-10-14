from polygon import Polygon

from sharp import Shape

class Square(Polygon,Shape):
    def area(self):
        return self.get_width()*self.get_height()