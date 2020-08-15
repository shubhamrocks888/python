with open("abc.txt",'r') as file:
    data = file.read()
    with open("demo.txt",'w') as f:
        f.write(data)

x = open("demo.txt",'r')
print (x.read())
