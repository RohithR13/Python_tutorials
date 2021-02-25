# slicing
digits =[0,1,2,3,4,5,6,7,8,9]

print(digits[:3])
print(digits[0:9])
print(digits[:-3])
print(digits[0:-9])
print(digits[5:])
#striding

print(digits[0:10:2])
print(digits[::-2])
for i in range(len(digits)):
    print(digits[0:i])

for i in range(len(digits)):
    print(digits[0:-i])
# for i in range(len(digits)):
#     print(digits[])
chunk_size=3
for i in range(len(digits)-(chunk_size-1)):
    print(digits[i:i+chunk_size])

