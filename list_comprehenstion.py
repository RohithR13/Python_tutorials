#list datastructure
names = ["raju", "ram", "raj"]
l = list()
for person in names:
    l.append(person)

print(l)

print([person for person in names])

print([person + " is hero"for person in names ])