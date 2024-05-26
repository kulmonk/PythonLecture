message ='Hello world'

print(message)

msg ='kuldeep\'s word'

print(msg)

m ="kuldeep's is happy men"

print(m)


msg1 = """kuldeep workd world is good  i am very happy """

print(msg1)

print(len(message))

#slicing
print(message[0])

print(message[10])

print(message[0:5])

print(message[0:5]) # first index is inclusive and second index is not 


print(message[:5])

print(message[6:])


print(message.lower())

print(message.upper())

print(message.count('H'))

print(message.find('w'))

new_msg = message.replace('world', 'kuldeep')

print(new_msg)

greenting ="Good Morning"
name = "kuldeep"

cont_msg = greenting + ','+ name

print(cont_msg)

cont_msg = '{}, {}. Welcome !'.format(greenting,name)

print(cont_msg)