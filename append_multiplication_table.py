## This code generates a multiplication table for a given number and appends it to a file.
n = int(input("Enter the number of elements in the list: "))

table = [n*i for i in range(1, 11)]
print(table)
with open('tables.txt','a')as f:
    f.write(str(table) + '\n')