#Sample code for using scope

# Function 1
# Scope
a = 0
b = 2
c = 1

def test():
    print(a)
    print(b)
    print(c)
test()

def test2():
    print(a / c)
    print(b * a)
    print(c + a)
test2()

#Scope - statements
def test3():
    if a != a:
        print("a is not equal to a")
    elif a == b:
        print("a is equal to b")
    else:
        print("Dude I don't know man!")
test3()

#Functions - optional & required w/ passing...
def test4():
    return a // 5
def test4_1():
    return b % c
d = test4()
e = test4_1()
f = d + e
print(f)
test4()
test4_1()

def test5(a, b, c, g=4, k=2, uh=0):
    return a + b + c + g + k + uh
result = test5(a, b, c)
print(result)
