def factorial(num):
    """This function calls itself to find
    the factorial of a number"""

    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))


num = 5
print("Factorial of", num, "is: ", factorial(num))