# #function syntax
# def function_name(parameters):
#     #function body
#     return value

#function greeting
def greeting(name, role):
    return f"Hello, {name}! You are a {role}."


greet1 =greeting("amrit", "developer")
print(greet1)
#snake case
def calculate_area(radius):
    import math
    area = math.pi * radius ** 2
    return area
#descriptive function name
def calculate_area_of_circle(radius): # radius is a parameter
    import math
    area = math.pi * radius ** 2
    return area

area1 = calculate_area(5) # 5 is an argument
print(f"The area of the circle with radius 5 is: {area1:.2f}")
# three parameters
def calculate_rectangle_area(length, width=1):
    area = length * width
    return area

area2 = calculate_rectangle_area(10, 5) # 10 is the length, 5 is the width
print(f"The area of the rectangle with length 10 and width 5 is: {area2}")
area3 = calculate_rectangle_area(10) # 10 is the length, width defaults to 1
print(f"The area of the rectangle with length 10 and default width is: {area3}")
#return expression
def calculate_square_area(side):
    return side * side

area4 = calculate_square_area(5) # 5 is the side
print(f"The area of the square with side 5 is: {area4}")

# * args and **kwargs
def print_arguments(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_arguments(1, 2, 3, name="Alice", age=30)

# * vs / 
def calculate_area_of_rectangle(length, width):
    return length * width   
area5 = calculate_area_of_rectangle(10, 5) # 10 is the length, 5 is the width
print(f"The area of the rectangle with length 10 and width 5 is: {area5}")
def create_user_profile(name, **additional_info):
    return {
        "name": name,
        "age": additional_info.get("age"),
        "email": additional_info.get("email")
    }

global_name = "Global Name"
def display_global_name():
    global global_name
    global_name = "Local Name"
    print(global_name)  # Accessing global variable
# local scope of variables
def outer_function():
    outer_variable = "I am an outer variable"
    
    def inner_function():
        inner_variable = "I am an inner variable"
        print(outer_variable)  # Accessing outer variable
        print(inner_variable)  # Accessing inner variable
    
    inner_function()        
outer_function()    
    # print(inner_variable)  # This will raise an error because inner_variable is not accessible here

def make_bold(text):
    return f"<b>{text}</b>"


def make_italic(text):
    return f"<i>{text}</i>"


@make_bold
def get_announcement():
    return "sample announcement"

calculate_tax = lambda income: income * 0.2
print(calculate_tax(50000))  

get_volume = lambda length, width, height: length * width * height
print(get_volume(2, 3, 4))

#map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#filter()
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

#sorted()
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]

def calculate_salary(hours_worked: float, hourly_rate: int) -> float:
    """Calculate the total salary based on hours worked and hourly rate."""
    return hours_worked * hourly_rate