## square_list_lambda.py
# Output: {'name': 'Bob', 'age': 25}
l = [1,2,3,4,5]
square = lambda x: x*x
sqlist = map(square, l)
print(list(sqlist))