# This code prints the elements at indices 2, 4, and 6 from the given list.
list = [2,5,8,9,6,3,88,1,7,4]
for i,item in enumerate(list):
    if i == 2 or i == 4 or i == 6:
        print(item)