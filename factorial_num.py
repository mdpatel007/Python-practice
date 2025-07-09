# This code calculates the factorial of a number entered by the user.
n = int(input("Enter a number: "))
product = 1
for i in range(1, n + 1):
    product = product * i
print("Factorial of", n, "is:", product)
