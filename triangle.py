from polygon import Polygon

from sharp import Shape

#Remenber to mention the Shape class beacause we have imported it and must be 
#use the imported module funcion

class Triangle(Polygon,Shape):
    def area(self):
        return self.get_width()*self.get_height()*1//2