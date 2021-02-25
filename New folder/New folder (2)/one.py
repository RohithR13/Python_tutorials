from itertools import combinations
a,value =input().split(" ")
for i in range(int(value)+1):
    sort =[]
    sort =sorted(list(combinations(a,int(i))))
    for _ in sort:
        print(''.join(_))
