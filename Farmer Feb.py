# cook your dish here
from sympy import * 
for _ in range(int(input())):
    x,y = map(int, input().split())
    z = x + y
    w = z + 1
    while isprime(w) != True:
        w += 1
    print(w - z)
