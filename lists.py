l = [1,2,3]
a = [1,"hello",4.5,True,[1,2,3]]

print(l)

print(a)
print(l[2])

names= ["raj","ram","raju"]
print(names)
names.append("rammu")
print(names)
names.insert(2,"ravi")
print(names)
names.remove("raj")
print(names)
names.reverse()
print(names)
number =[5,6,99,354,46,69,47,33,8,4,7]

print(number)
number.sort()
print(number)
for number in number:
    print(number)


# le = int(input("enter the length of the string:"))
# dataInput=[]
# for i in range(le):
#    data =int(input("give input to the list:"))
#    dataInput.append(data)
    
# print("your  list",dataInput)

le = int(input("enter the length of the string:"))
dataInput=[]
for i in range(le):
   
   dataInput.append(int(input("give input to the list:")))

print("the list:",dataInput)
print(dataInput[1])