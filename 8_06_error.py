# while True:
#     try:
#         a = int(input("enter a first number:"))
#         b = int(input("enter a second number:"))


#         print(f"the divison is {a / b}")

#     except NameError:
#         print("hey give correct input.")

#     except ValueError:
#         print("please dont perform bad typecast")

#     except ZeroDivisionError:
#         print("dont divide by zero")


#     except Exception as e:
#         print("some error ouccred", e)


a = int(input("the value of a:"))
b = int(input("value of b:"))

if b==0 :
    raise ValueError("please do not divide by 0")

print(f"the divison is {a/b}")