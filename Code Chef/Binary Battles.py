# cook your dish here
import math
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    for i in range(1,21):
        if 2**i==n:
            n=i
            break
    print((n*a)+(n-1)*b)
