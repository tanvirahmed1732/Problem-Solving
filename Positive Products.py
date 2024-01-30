# Positive Products
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    cp = 0
    cn = 0
    sm = 0
    for i in range(n):
        if s[i]>0:
            cp += 1
        elif s[i]<0:
            cn += 1
    for i in range(cp):
        sm += i 
    for i in range(cn):
        sm += i 
    print(sm)
