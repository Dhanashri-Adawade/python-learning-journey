import os

new = os.listdir("dir")
print(new)

new1 = os.getcwd()
print(new1)

print(os.path.exists("dir1"))
# os.rmdir("dir")
os.remove("dir")