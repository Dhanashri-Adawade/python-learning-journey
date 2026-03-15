class Animal:

    def Sound(self):
        print("Some sound")

class Dog(Animal):
    def Sound(self):
        super().Sound()
        print("Bark")


d = Dog()
d.Sound()