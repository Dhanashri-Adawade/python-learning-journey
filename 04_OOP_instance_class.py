class Employee:

    def __init__(self, salary, name, bond,company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company= company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"the name is {self.name}. and the salary is {self.salary} also bond is {self.bond}and the company is {self.company}")

e1 = Employee(34000, "Hernry", 7,"jdj")
# print(e1.get_salary())
print(e1.company)
e1.get_info()

print(dir(e1)) #will always print instance attribute whenever present
print(Employee.company) # this will alwasy print the class attribute.