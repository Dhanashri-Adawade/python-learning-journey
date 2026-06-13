class Employee:

    def __init__(self, name, age):
        self.nam = name
        self.ag = age

    def __str__(self):
        return f"the name is {self.nam} and the age is {self.ag}"
    
    def __repr__(self):
        return f"name: {self.nam}\n age: {self.ag}"
    
    def __len__(self):
        return len(self.nam)

e = Employee('Dhan', 20)
e1 = Employee('rahul', 13)

print(e.nam,e.ag)

print(str(e1))
print(repr(e))
print(len(e))       