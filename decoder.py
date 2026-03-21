# decorator is function that takes a function, it creates a new function inside its body (wrapper). then it returns that new function.
def decorater(func):
    def wrapper():
        print("I am about to execute the functions")
        func()
        print("I am executed")
    return wrapper

@decorater
def info():
    print("Hey I am dhanshri ")

info()


# f=decorater(info) # object is created
# f()