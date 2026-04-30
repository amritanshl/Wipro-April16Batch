#try
#except
#else
#finally
# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(message)s | datefmt=%Y-%m-%d %H%M%S ')
# logger = logging.getLogger("USER VALIDATION")
# def divide_numbers(a, b):
#     try:
#         result = a / b
   
#     # except ZeroDivisionError:
#     #     logging.error(f"Attempt to divide {a} by zero")
#     #     return "Error: Division by zero is not allowed."
#     except Exception as e:
#         logging.critical(f"SOME EXCEPTION AS {e}")
#         return f"Error: {e}"
#     else:
#         print("Error")
#         return f"The result of {a} divided by {b} is {result}."
#     finally:
#         print("Execution of divide_numbers function is complete.")

# print(divide_numbers(10, 2))
# print(divide_numbers(10, 0))

#DEBUG



#raise exception
import logging
import time

# 1. THE POWER SWITCH (Logging Configuration)
# This tells Python HOW to write logs, WHERE to send them, and WHAT level to care about.
logging.basicConfig(
    level=logging.DEBUG, # We set to DEBUG to see every single detail
    format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger("AppService")

# 2. LOGIC WITH EXCEPTIONS
def validate_age(age):
    logger.debug(f"Validating age: {age}") # Breadcrumb for developers
    if age < 0:
        logger.warning(f"Suspicious Activity: Negative age entered ({age})")
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        logger.info(f"Access Denied: User is {age} (Minor)")
        raise ValueError("Age must be at least 18.")
    else:
        return f"Valid age: {age}"

def withdraw(amount, balance):
    logger.debug(f"Attempting withdrawal: ${amount} from balance: ${balance}")
    if amount > balance:
        # We use ERROR here because this is a failed business transaction
        logger.error(f"Transaction Failed: Overdraft attempt of ${amount}")
        raise ValueError("Insufficient funds.")
    else:
        new_balance = balance - amount
        logger.info(f"Transaction Success: ${amount} withdrawn.")
        return new_balance

# 3. THE "TERMINAL ANIMATION" (Execution Block)
print("--- STARTING SYSTEM SIMULATION ---\n")

# Scenario A: The Negative Age Bug
try:
    print(f"Result: {validate_age(-5)}")
except ValueError as ve:
    logger.error(f"Caught at User Interface: {ve}")
finally:
    print("Check 1 Complete.\n")
    time.sleep(1) # Small pause for 'animation' effect

# Scenario B: The Successful Withdrawal
try:
    current_balance = 1000
    new_bal = withdraw(200, current_balance)
    print(f"Successfully updated balance to: ${new_bal}")
except ValueError as ve:
    logger.error(f"Transaction halted: {ve}")
else:
    # This only runs if the try block succeeded!
    logger.info("Emailing receipt to user...")
finally:
    print("Check 2 Complete.\n")
    time.sleep(1)

# Scenario C: The Insufficient Funds Error
try:
    withdraw(5000, 800)
except ValueError as ve:
    logger.error(f"Caught at ATM Interface: {ve}")
finally:
    print("Check 3 Complete.\n")

print("--- ALL PROCESSES FINISHED ---")