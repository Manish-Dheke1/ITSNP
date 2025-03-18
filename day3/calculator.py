"""
This module contains function for arithmetic operation

"""


from arithmetic_operations import add, diff

try:
    num1 = int(input('Enter first number:'))
    num2 = int(input('Enter second number:'))
except ValueError:
    print("Invalid input")

    # Ask user what to do with input
    operation = input("Enter operation: + for sum, - for difference ")

    if operation == "+":
        result = add(num1, num2)

    elif operation == "-":
        result  = diff(num1, num2)

        
    else:
        result = "Invalid operation"

    print(f"Result: {result}")




# def add(num1, num2):
#     print("For sum")
#     return num1 + num2

# def diff(num1, num2):
#     print("For difference")
#     return num1 - num2

