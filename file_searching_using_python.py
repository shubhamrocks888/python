import os

cwd = os.getcwd()

for path,dir,files in os.walk(cwd):
    for file in files:
        if file.endswith('.py'):
            print (path + "\\" +  file)
