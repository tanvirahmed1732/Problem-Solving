# Prime Generator
from sympy import *
for k in range(int(input())):
    i,n = map(int, input().split())
    for j in range(i,n+1):
        if isprime(j):
            print(j)
    print()
