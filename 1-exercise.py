# 1. The Inventory Surplus
# You have stock = 100 and orders = 45. Write an expression to find how many items are left, then use a comparison operator to check if the remaining stock is greater than 50.

# Solution: remaining = stock - orders (Subtraction). Then print(remaining > 50). Since 55 is greater than 50, the output is True.
stock = 100
orders = 45 
#find remaining stock
remaining = stock - orders
#check if remaining stock is greater than 50
print(remaining > 50)  # Output: True