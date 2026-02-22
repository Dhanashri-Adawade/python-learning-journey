new_list = [89,90, "harry","jonny", 76]

list11 = [78,34,76]
list11.sort()
print(list11)
# new_list.append("Hari") # this will change the orignal list 
# print(new_list)

# new_list.pop()
# print(new_list)

new_list.insert(1,23) # here 23 will be added at first position.
print(new_list)
# new_list.extend(list11)
# print(new_list)
list11.extend(new_list)
print(list11)