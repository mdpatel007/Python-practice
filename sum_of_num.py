#This code calculates the sum of numbers from 1 to n, where n is entered by the user.
n = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("Sum of numbers from 1 to", n, "is:", sum)