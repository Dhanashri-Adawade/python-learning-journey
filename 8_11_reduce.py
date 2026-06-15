# from functools import reduce

# a = [2,3,45,6]
#     #[5, 45, 6]
#     #[50, 6]
#     #[56]
# def sum(a,b):
#     return a*b

# c = reduce(sum, a)
# print(c)
from functools import reduce

a = [34,56,78]

def mul(a,b):
    return a*b
c = reduce(mul, a)
print(c)
