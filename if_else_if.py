age = int(input("Enter your age:"))

if(age>18):
    print("You are eligible for vote")
elif(age==18):
    print("we think on it")
elif(age==0):
    print("hey you are just born")
else:
    print("You are not eligible for vote")