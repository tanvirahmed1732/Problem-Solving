# https://www.codechef.com/problems/PASCRO
import math
for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    t=0
    c=0
    for i in range(n):
        if a[i]==b[i]:
            continue        
        if a[i]=='R' and b[i]=='S':
            c+=1
        elif a[i]=='S' and b[i]=='P':
            c+=1
        elif a[i]=='P' and b[i]=='R':
            c+=1
        t+=1
    t=t//2
    if t<c:
        print(0)
    else:
        print(t-c+1)
