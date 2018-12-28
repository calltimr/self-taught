class Square:
    square_list=[]
    def __init__(self,s):
        self.side = s
        self.square_list.append(self)

    def __repr__(self):
        return (str(self.side)+" by ")*3 + str(self.side)

def is_same_obj(obj_a,obj_b):
    return obj_a is obj_b

my_square = Square(4)
print(my_square)
my_square_too = Square(5)
print(my_square_too)
#print(Square.square_list)

print(is_same_obj(my_square,my_square_too))
