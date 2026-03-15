class Person:

    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return f"the name is {self.name}, and age is {self.age}"


p = Person("rahul",3)
print(p.info())

#OR

print(p.name,p.age)


