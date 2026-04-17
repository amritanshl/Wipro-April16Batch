print("Create a advanced python calculator matching the operator with if, elif and else statements")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, ^): ")
num2 = float(input("Enter second number: "))
#sytax of match statement
match operator:
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    case "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    case "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    case "^":
        result = num1 ** num2
        print(f"{num1} ^ {num2} = {result}")
    case _:
        print("Error: Invalid operator. Please use one of the following: +, -, *, /, ^.")
