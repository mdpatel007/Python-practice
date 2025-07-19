class Employee:
    a = 1

    @classmethod
    def show(self):
        print("Class method called")
        print(self.a)

e = Employee()
e.a = 45

e.show()  # This will call the class method and print the class variable 'a'