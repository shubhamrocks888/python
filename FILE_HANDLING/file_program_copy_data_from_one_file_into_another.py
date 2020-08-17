#Copy whole data
with open("abc.txt",'r') as file:
    data = file.read()
    with open("demo.txt",'w') as f:
        f.write(data)


                '''OR'''
#Copy line by line

with open("abc.txt",'r') as file:
    with open ("demo.txt",'w') as f:
        for line in file:
            f.write(line)
        
