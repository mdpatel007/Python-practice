## This code reads the contents of three files and prints them.
try:
    with open('func.py', 'r') as file:
        content = file.read()
        print(content)
except Exception as e:
    print(e)

try:
    with open('ch_9.py', 'r') as file:
        content2 = file.read()
        print(content2)
except Exception as e:
    print(e)

try:
    with open('demo.txt', 'r') as file:
        content3 = file.read()
        print(content3)
except Exception as e:
    print(e)


finally:
    print("Thank you.")
    
