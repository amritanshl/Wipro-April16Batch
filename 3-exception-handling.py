#try
#except
#else
#finally
def divide_numbers(a, b):
    try:
        result = a / b
    except Exception as e:
        return f"Error: {e}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"The result of {a} divided by {b} is {result}."
    finally:
        print("Execution of divide_numbers function is complete.")

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))

#raise exception
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise ValueError("Age must be at least 18.")
    else:
        return f"Valid age: {age}"
try:
    print(validate_age(25))
    print(validate_age(-5))
except ValueError as ve:
    print(f"Validation Error: {ve}")

def withdraw(amount, balance):
    if amount > balance:
        raise ValueError("Insufficient funds.")
    else:
        return f"Withdrawal successful. Remaining balance: {balance - amount}"
    
    