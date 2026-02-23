coordinates= (23,45)
print(coordinates)

print(coordinates[0])
print(coordinates[1])

# coordinates[0]=67
# print(coordinates)

new = list(coordinates) # convert tuple into list
new[0]= 50
print(new)

new_coordinates =tuple(new)
print(new_coordinates)