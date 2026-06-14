def divide(a, b):
        try:
            c =  a/b
            print(c)
            return c


        except Exception as e:
            print(e)
            return None

        finally:
            print("this is always executed")

a = int(input("the value of a:"))
b = int(input("value of b:"))

divide(a,b)