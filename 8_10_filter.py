a = [34,7,3, 4,23,45]

# def fun(x):
#     if x>9:
#         return True
#     else:
#         return False
    
new = list(filter(lambda x : x>9, a))

print(new)