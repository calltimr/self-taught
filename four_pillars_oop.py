class Shape():
    def what_am_i(self):
         print("I am a shape")

class Rectangle(Shape):
    pass
"""
    def __init__(self,s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4
"""
class Square(Shape):
    pass
"""
    def __init__(self,s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self,c):
        self.side += c
        return self.side
"""
"""     
class Shape():
#    def __init__(self):
     def what_am_i(self):
         print("I am a shape")
#    def what_am_i(self):
#        print("I am a shape")
        
#rectangle = Rectangle(4)
#print(rectangle.calculate_perimeter())
#square = Square(2)
#print(square.calculate_perimeter())
#print(square.change_size(-1))
"""
shape = Shape()
shape.what_am_i()
square = Square()
square.what_am_i()
rectangle = Rectangle()
rectangle.what_am_i()
