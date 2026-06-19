# context manager

with open("d.txt","r") as f:   
    new = f.read()
    print(new)

    # no need to closed file because file was automatically deleted by using with.