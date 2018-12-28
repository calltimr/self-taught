Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World!")
Hello World!
>>> print("Hello, World!")
Hello, World!
>>> 
=================== RESTART: D:/self-taught/hello_world.py ===================
Hello, World!
>>> 
=============================== RESTART: Shell ===============================
>>> 
=============================== RESTART: Shell ===============================
>>> print("Hello")
Hello
>>> for i in range(100)
SyntaxError: invalid syntax
>>> for i in range(100):
	print("HEllo, World!")

	
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
HEllo, World!
>>> 
============= RESTART: D:/self-taught/calc_rectangle_diagonal.py =============
>>> l
4
>>> w
10
>>> d
10.04987562112089
>>> 
=============================== RESTART: Shell ===============================
>>> 2 + 2>>> l
4
>>> w
10
>>> d
10.04987562112089
>>>
SyntaxError: invalid syntax
>>> 2+2
4
>>> 2-1
1
>>> 6*6
36
>>> 10/2
5.0
>>> 10/0
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    10/0
ZeroDivisionError: division by zero
>>> x=100
>>> x
100
>>> # x is a variable
>>> x
100
>>> # incrementing +=
>>> x
100
>>> x+=3
>>> x
103
>>> boolean=true
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    boolean=true
NameError: name 'true' is not defined
>>> boolean = True
>>> boolean
True
>>> # decrementing 'subtracting'
>>> x-=5
>>> x
98
>>> hw="Hello, World!"
>>> hw
'Hello, World!'
>>> # variable names may contain letters, numbers, and _
>>> # variable may contain an _ as 1st position, 'special type'
>>> 8*9
72
>>> # data types in python: 1 as integer, "hello" as string, 15.4 as float, true as boolean
>>> # None as nonetype
>>> 
>>> # everything in python is an object and every object has a data type
>>> # integer int data type
>>> # decimal 9.8 is data type float
>>> # strings in str data type
>>> # booleans True, False in bool data type
>>> # also datatype Nonetype exists represents an absence of a vale
>>> # every object has a category or a data type
>>> 
>>> # python has 3 types of operators:  arithmetic, comparison, and logical operators
>>> # arithmetic operators are used in an expression
>>> # python reduces an expression to a single value
>>> # an expression is made up of operands and operators
>>> # python has operators: ** exponent, % modulo, // integer division, / division
>>> #	* multiplication, + addition, - subtraction
>>> 
>>> # dividing produces a quotient and a remainder  ex. 10/3 3,1
>>> # modulo operator 10%3 produces the remainder 1, modulo 2 operation determines even,odd
>>> #	value 12%2=0 so even, 13%2=1 so odd
>>> # 13//5 produces the quotient or 2
>>> # arithmetic operations order
>>> # Please Excuse My Dear Aunt Sally => parentheses, exponents, mult, div, add, sub
>>> a=4
>>> b=2
>>> a%2
0
>>> a//2
2
>>> a//b
2
>>> a=5
>>> a%2
1
>>> a//b
2
>>> a%b
1
>>> 2**3
8
>>> 

Note*  line of code can be spread over more lines by surrounding it in
	three quotes, parenthesis, brackets, and braces
ex	print("""This is a re
		ally really long line of code
		.""")
or a \ backslash
	print\
	("""This is a re
	ally long line""") 

Note* spacing Python uses indent 4 spaces to signify begin/end of code blocks
for i in range(100):
	print("hello")