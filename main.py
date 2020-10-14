from square import Square as sq
from triangle import Triangle as tr

#Square
 
s1=sq()
s1.set_value(8,15)
s1.set_color("Blue")
print(s1.area(),s1.get_color())

#Triangle

s2=tr()
s2.set_value(8,15)
s2.set_color("Green")
print(s2.area(),s2.get_color())