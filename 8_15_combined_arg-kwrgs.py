def combined(*args, **kwargs):
    print(args)
    print(kwargs)

    for i in kwargs.keys():
        print(f"the marks of {i} are {kwargs[i]}")

print(combined(2,4,5, bina=89, reeta= 80))