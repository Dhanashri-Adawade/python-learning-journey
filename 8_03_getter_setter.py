class Employee:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    # def info(self):
    #     print(f"my name is {self.name} and age is {self.age}")
    @property
    def first_name(self):
        fn = self.name.split(" ")
        print(fn)
        print(fn[0])


    def lnane(self):
        ln = self.name.split(" ")
        print(ln[1])
                        

    def set_name(self, first):
        # self.first = first
        l = self.name.split(" ")
        chg_first = f"{first} {l[1]}"
        self.name = chg_first

e = Employee('Aranav Jadeja', 20)
# e.project = 10
# e.name1 = 'rina'
# print(e.project)
# print(e.name1) 
# print(e.age) 
# e.info()
print(e.first_name())
# e.lnane()
# e.set_name('Dhanu')