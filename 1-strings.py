text = "Hello, World!"
print(text[2:5])  # Output: llo
print(text[:5])   # Output: Hello
print(text[7:])   # Output: World!
print(text[-6:])  # Output: World!
print(text[::2])  # Output: Hlo ol!



#[start:stop:step]
name = " Python Programming                                                                                                                                                                                                                                                     "
number = 42
print(name.strip() + str(number))  # Output: Python Programming42
print(name.upper().strip())  # Output: PYTHON PROGRAMMING
print(name.lower().strip())  # Output: python programming   
print(name.replace("Python", "Java").strip())  # Output: Java Programming

print(f"{name.strip()} {number}")  # Output: Length of name: 18
#print(f"Is 'Python' in name? {'Python' in name}")  # Output
price = 19.99
tax_rate = 0.07

print(f"Total price including tax: ${price * (1 + tax_rate):.2f}")  # Output: Total price including tax: $21.39


text = "this is a \"sample\" string for testing."
print(text)  # Output: this is a "sample" string for testing.
# \'
print('It\'s a nice day!')  # Output: It's a nice day!
# \\
print("This is a backslash: \\")  # Output: This is a backslash: \
# \n    
print("Line 1\nLine 2")  # Output: Line 1
                          #         Line 2
# \t
print("Column 1\tColumn 2")  # Output: Column 1    Column 2 
#\0
print("Null character:\0End")  # Output: Null character:End

#Shopping List:
#   - Apples
#   - Bananas
shopping_list = "Shopping List:\n\t- Apples\n\t- Bananas"

# isDigit() method
print("12345".isdigit())  # Output: True
print("123a5".isdigit())  # Output: False

#isAlpha() method
print("Hello".isalpha())  # Output: True        
print("Hello123".isalpha())  # Output: False

#islower() method
print("hello".islower())  # Output: True
print("Hello".islower())  # Output: False

#isupper() method
print("HELLO".isupper())  # Output: True
print("Hello".isupper())  # Output: False

#startswith() method
print("Hello, World!".startswith("Hello"))  # Output: True
print("Hello, World!".startswith("World"))  # Output: False
#endswith() method
print("Hello, World!".endswith("!"))  # Output: True    
print("Hello, World!".endswith("World"))  # Output: False
#find() method
print("Hello, World!".find("World"))  # Output: 7
print("Hello, World!".find("Python"))  # Output: -1
#count() method
print("Hello, World!".count("l"))  # Output: 3
print("Hello, World!".count("o"))  # Output: 2