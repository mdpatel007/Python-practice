# This code prints a pattern of stars and spaces in a pyramid shape.
'''
Enter a start num: 5
*    
**
***
****
*****
'''
n = int(input("Enter a start num: "))
for i in range(1, n+1):
    print("*" * (i), end="")#stars
    print(" " * (n - i), end="")#space before stars
    print()