a=[10,16,20,15]
b =[i for i in a]
print(b)

'''
lists=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
        
    lists.append([score, name])

lists.sort()


a = [i for i in lists if i[0] != lists[0][0]]
c = [j for j in a if j[0] == a[0][0]]
c.sort(key=lambda x: x[1])

for i in range(len(c)):
   print(c[i][1])
'''

def print_rangoli(size):
    from string import ascii_lowercase as chars
    heap = [(('-'.join(chars[i:n])[::-1]+'-'.join(chars[i:n])[1:])).center(4*n-3, '-')for i in range(n)]
    print(*(heap[::-1]+heap[1:]), sep="\n")

n =int( input(" enter size:"))
print_rangoli(n)