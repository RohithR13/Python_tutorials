f = open("mydata.txt",'r')
#print(f.read())
print(f.readline(), end="")



with open('abc.txt','a+') as f1:
    f1.write(input("write input"))
 
with open('abc.txt','r') as f1:
    print(f1.read())

