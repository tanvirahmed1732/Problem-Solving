# https://www.codechef.com/problems/EVMHACK
for _ in range(int(input())):
    a,b,c,p,q,r=map(int,input().split())
    x,y,z=p-a,q-b,r-c
    sm=0
    if x>=y and x>=z:
        sm=p+b+c
    elif y>=x and y>=z:
        sm=a+q+c
    else:
        sm=a+b+r
    if sm>(p+q+r)/2:
        print("YES")
    else:
        print("NO")
