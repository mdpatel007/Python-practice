class Demo:
    a = 4 

o = Demo()
print(o.a) # Prints the class attribute because instance attribute is not present
o.a = 0  # Instance ttribute is set
print(o.a) # Prints the instance attribute because instance attribute is present
print(Demo.a) # Preints the class attribute