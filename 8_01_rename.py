# decorator is a function  that takes a function, and its create a new function inside its body(wrapper). then its return that new  function. 

def decorator(func):
    def wrapper():
        print("good morning")
        func()
        print("good morning")
    return wrapper

@decorator
def intro():
    print("hello")
intro()

# f = decorator(intro)
# f()