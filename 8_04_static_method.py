class Employee:
    mark = 20 
    age=45
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        # print(f"the name is {self.name} and salary is {self.salary}")
        return f"the name is {self.name} and salary is {self.salary}"

    # def sum(self,a,b):
    #     return a+b

    @staticmethod  #staticmethod this method does not need self 
    def sum(a,b):
        return a+b
    
    @classmethod     #
    def class_new(cls):
        print(cls.mark)


    @classmethod
    def age_new(a):
        print(a.age)


    @classmethod
    def age_change(a1, new):
        a1.age = new

e =  Employee("Aayush dawwal", 25200)
e1 =  Employee("Anushka", 38000)
print(Employee.mark)


# e.info()
print(e.info())
print(e1.info())
print(e1.sum(9,5))
e1.class_new()
e1.age_new()

e1.age_change(50)
e1.age_new()