#arithmetic operators
a = 10
b = 5   
print(a + b)  # Output: 15
print(a - b)  # Output: 5
print(a * b)  # Output: 50
print(a / b)  # Output: 2.0
print(a // b) # Output: 2
print (10//3) # Output: 3
print(10/3) # Output: 3.3333333333333335
print(a % b)  # Output: 0
print(a ** b) # Output: 100000
#comparison operators
print(a == b)  # Output: False
print(a != b)  # Output: True   
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

#Logical Operators
x = True
y = False
print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False 
# not>and>or
print(not x and y)  # Output: False

# Identity Operators
print(x is y)   # Output: False
print(x is not y)  # Output: True
print(x is True)  # Output: True
print(y is False)  # Output: True
#is vs ==
a = [1, 2, 3]   
b = [1, 2, 3]
print(a == b)  # Output: True (values are equal)
print(a is b)  # Output: False (different objects in memory)
c = a       
print(a is c)  # Output: True (same object in memory)

if x is None:
    print("x is None")
if x == None:
    print("x is None")

#Membership Operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False

text = "Hello, World!"
print('H' in text)  # Output: True
print('h' in text)  # Output: False
print('W' in text)  # Output: True
print('w' in text)  # Output: False

#bitwise operators
a = 5  # In binary: 0101
b = 3  # In binary: 0011
print(a & b)  # Output: 1 (In binary: 0001)
print(a | b)  # Output: 7 (In binary: 0111)
print(a ^ b)  # Output: 6 (In binary: 0110)
print(~a)     # Output: -6 (In binary: ...1111010)
print(a << 1) # Output: 10 (In binary: 1010)
print(a >> 1) # Output: 2 (In binary: 0010)