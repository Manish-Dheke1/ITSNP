"""
define a function
that takes two arguments
and returns their sum, product and difference
as a tuple
accepts a default argument
"""

def calculate_sum_product_difference(num1, num2= 6, *numbers, **kwargs):
    if kwargs.get("stop"):
        print("Breaking")
        return 0
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    i = 1
    for num in numbers:
        print(i)
        sum += num
        difference -= num
        product *= num
        i += 1
    return f"Sum: {sum}", f"Difference: {difference}", f"Product: {product}"

print(calculate_sum_product_difference(1, 2, 3))



# def calculate_sum_product_difference(num1, num2, *numbers):
#     sum = num1 + num2
#     difference = num1 - num2
#     product = num1 * num2
#     return sum, difference, product

# print(calculate_sum_product_difference(1, 2, 3))












# sum = lambda x, y: x + y

# print(sum(1, 2))
