## Property Decorators in Python
class Employee:
    salary = 1000
    incremeant = 20

    @property
    def salary_after_increment(self):
        return (self.salary + self.incremeant * (self.incremeant/100))
    
    @salary_after_increment.setter
    def salary_after_increment(self, new_salary):
        self.incremeant = (new_salary - self.salary) / self.salary * 100

e = Employee()
e.salary_after_increment = 1220.0 
print(e.incremeant) # Output: 22.0