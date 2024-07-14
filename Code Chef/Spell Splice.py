# Spell Splice
for _ in range(int(input())):
    n=int(input())
    a=[0]*n
    b=[0]*n
    for i in range(n):
        b[i],a[i] = map(int,input().split())
    m = 0
    for i in range(n):
        for j in range(i+1,n):
            temp = b[i]*a[j] + a[i]*b[j]
            if temp>m:
                m = temp
    print(m)
