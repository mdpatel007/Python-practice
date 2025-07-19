# def http_status(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown Status"
        
# print(http_status(505))  # Output: OK

# from typing import List,Tuple,Dict,Union

# numbers: List[int] = [1, 2, 3, 4, 5]

# person: Tuple[str, int] = ("Alice", 30)

# score: Dict[str,int] = {"Alice": 90, "Bob": 85}

# Indentifier : Union[int,str] = "1020MIHIR"
# indentifier = 12345
# print(list(numbers))
# print(tuple(person))
# print(score)
# print(Indentifier)
# print(indentifier)

dict1 = {"name": "Alice", "age": 30}
dict2 = {"f_name": "Bob", "f_age": 25}
merged = dict1 | dict2
print(merged)  # Output: {'name': 'Bob', 'age': 25