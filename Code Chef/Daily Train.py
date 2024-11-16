# https://www.codechef.com/problems/DAILY
import math
x,n=map(int,input().split())
ans=0
for i in range(n):
    s=input()
    m=0
    n=54
    temp=''
    for j in range(9):
        temp=s[m:m+4]+s[n-2:n]
        c=temp.count('0')
        ans+=math.comb(c,x)
        m+=4
        n-=2
print(ans)
