"""
class Apple:
    def __init__(self,c,w,h,cir):
        self.color=c
        self.weight=w
        self.height=h
        self.circumference=cir

apple=Apple("green",3,3,4)
print(apple.color)
print(apple.weight)
print(apple.height)
print(apple.circumference)


import math

class Circle:
    def __init__(self,r):
        self.radius = r
        self.area = math.pi * r * r
        

circle=Circle(4)
print(circle.area)


class Triangle:
    def __init__(self,b,h):
        self.base = b
        self.height = h
        self.area = (b * h) / 2

triangle = Triangle(2,3)
print(triangle.area)
"""

class Hexagon:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 6

hexagon = Hexagon(3)
print(hexagon.calculate_perimeter())
        
