def sum(num1, num2):
    return num1 + num2

def calculate(*args, **kwargs):
    if kwargs.get == "method":
        if kwargs.get == "multiply":
            return args[0] * args[1]
            

    sum = 0
    for i in args:
        sum += i
    return sum

calculate(1, 2, 3, 4)
calculate(1, 2, 3, 4, 5)


calculate(method="multiply")


