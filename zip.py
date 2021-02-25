l1 = [1,2,3,4,5,6,7,8,9]
l2 =['one','two','three','four','five','six','seven','eight','nine']

zipped = dict(zip(l1,l2))

print(zipped)
list_zipped = list(zip(l1, l2))
print(list_zipped)

unzipped =list(zip( *list_zipped ))
print(unzipped)
