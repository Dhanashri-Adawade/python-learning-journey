x = {78,90,23,"good",2.5}
y = {23,2.5,"Morning"}

# z = y.union(x)
z = x.union(y) # all elements but not repeat
print(z)

w = x.intersection(y)# common in both
print(w)

v = x.difference(y) #elements preset in x but not in y
print(v)

v = y.difference(x)
print(v)