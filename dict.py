import os 

my_cuurent = os.getcwd()
my_cuurent

my_file =open('my_file.txt', 'r')

my_file.read()
my_file.read()

my_file.seek(0)

cont =my_file.read()
cont

my_file.readlines()

my_file.close()


with open('my_file.txt', 'r') as mynewfile:
    contents =mynewfile.read()

contents

with open('my_file_new.txt','w') as f:
    f.write("this is new file \n this is second")

my_file_new.txt.read()

my_iterable= [1,2,3]

for items in my_iterable:
    print(items)