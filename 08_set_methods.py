s = {"hii", 89, 7,45}

print(s)
s.add("hello")
s.add(90)
print(s)

s.remove(89)
print(s)

s.discard(30) # No error if element not found.
print(s)

s.pop() # removes random element.
print(s)