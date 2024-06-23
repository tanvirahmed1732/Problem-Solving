# Farmer And His Plot
import math
for _ in range(int(input())):
    n,m=map(int,input().split())
    if n<2 or m<2:
        print(n*m)
    else:
        print((m*n)//(math.gcd(m,n))**2)
