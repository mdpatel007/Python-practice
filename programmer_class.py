class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("prog",15000,18000)
print(p.name,p.salary,p.pin)
r = Programmer("parthiv",20000,25000)
print(r.name,r.salary,r.pin)