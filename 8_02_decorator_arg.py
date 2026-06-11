# def repeat(n):
#     def decorator(func):
#         def wrapper(a):
#             for i in range(n):
#                 func(a)
#         return wrapper
#     return decorator


# @repeat(3)
# def inro(a):
#     print(f"Namskar! {a}")

# inro("dhanu")

def repeat(n):
    def decorator(func):
        def wrapper(x):
            print("nice marks")
            for i in range(n):
                func(x)
        return wrapper
    return decorator

@repeat(7)
def stu(x):
    print("hello which sub you want to learn")

stu("Rohit")
