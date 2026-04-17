print("create advanced control flow with if, elif and else statements")
print("Create a advanced python calculator using if, elif and else statements")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, ^): ")
num2 = float(input("Enter second number: "))

if operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "^":
    result = num1 ** num2
    print(f"{num1} ^ {num2} = {result}")
else:
    print("Error: Invalid operator. Please use one of the following: +, -, *, /, ^.")
