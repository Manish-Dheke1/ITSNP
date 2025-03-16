"""
User input take
Ask user what to do with input
Based on user's response perform operation
Return result
"""

# Taking input from user
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

# Ask input from user
operation = input("Enter operation: + for sum, - for difference, * for multiplication, / for divide ")

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result  = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    result = num1 / num2
    
else:
    result = "Invalid operation"

print(f"Result: {result}")