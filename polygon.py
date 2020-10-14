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