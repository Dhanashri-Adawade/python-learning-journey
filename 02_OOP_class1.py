class Employee:
      brand="HP"

      def my(self): # self is important here because self is way to reference the object of the class which is being created.
           return 200
    
e = Employee() # here object of an class is created.
print(e.my())

e1 = Employee()
print(e.my())

print(e1.brand)