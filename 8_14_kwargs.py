# def marks(**kwargs):

#     #kwargs is a dictionary with all the key value pairs which were passed to marks  
#     for i in kwargs.keys():
#         print(f"the makrs  of the {i} is  {kwargs[i]}")

# marks(sonu=34, minu=56)

def color(**kwargs):
    for i in kwargs.keys():
        print(f"the color of {i} is {kwargs[i]}")

color(RK='red', VJ= 'voilet' )