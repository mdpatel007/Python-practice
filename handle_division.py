## This code handles division by zero error when dividing two numbers.
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a/b)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")