# N = int(input())
# lists =list()
# for _ in range(N):
#     query = input().strip().split()
#     command,*args =query[0],query[1:]
#     if(command=="print"):
#         print(lists)
#         continue
#     getattr(lists,command)(*(map(int,args[0])))

n =int(input())
for _ in range(n):
    for i in range(_):
        print(i,end=" ")
    print(" ")

print(" ")
for _ in range(n):
    for i in range(_):
        print(n,end=" ")
    print(" ")

print(" ")


print(" ")
for n in range(1,n+1):
    for i in range(1,n+1):
        print(1,end=" ")
    print(" ")