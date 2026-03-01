class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = bond
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"the name is {self.name}. and the salary is {self.salary} also bond is {self.bond}")

e1 = Employee(34000, "Hernry", 7)
# print(e1.get_salary())
e1.get_info()