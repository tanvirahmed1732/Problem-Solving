import sys
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=input()
    b=input()
    mn=sys.maxsize
    for i in range(n-m+1):
        k=i
        t=0
        for j in b:
            if j != a[k]:
                t+=1
            k+=1
        if t<mn:
            mn=t  
    print(mn)