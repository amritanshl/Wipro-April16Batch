# while condition:
#    # code to be executed

count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

password = ""
count = 0
while True:
    password = input("Enter the password: ")
    if password == "secret":
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")
        count += 1
        if count >= 5:
            print("Too many failed attempts. Access denied.")
            break

print("Create a advanced python calculator matching the operator with if, elif and else statements")


while True:
    user_input = input("Enter an expression (e.g., 2 + 3) or 'exit' to quit: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    match operator:
        case '+':
            result = num1 + num2
            print(f"The result is: {result}")
        case '-':
            result = num1 - num2
            print(f"The result is: {result}")
        case '*':
            result = num1 * num2
            print(f"The result is: {result}")
        case '/':
            if num2 != 0:   
                result = num1 / num2
                print(f"The result is: {result}")   
            else:
                print("Error: Division by zero is not allowed.")
        case _: 
            print("Invalid operator. Please use +, -, *, or /.")


