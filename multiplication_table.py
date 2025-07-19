## This code generates a multiplication table for a given number.
n = int(input("Enter the number of elements in the list: "))

table = [n*i for i in range(1, 11)]
print(table)