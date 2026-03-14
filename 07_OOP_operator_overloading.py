class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Vector(self.x + p.x, self.y + p.y)
    
    # This magic method triggers when you call print(object)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, p):
        return Vector(self.x + p.x, self.y + p.y)

p1 = Vector(2, 2)
p2 = Vector(4, 2)
# p = p1.sum(p2)
p =p1+p2 # we overloaded the + operator by writing __add__ function
print(p) # Output: Vector(6, 4)