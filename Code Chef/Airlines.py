# cook your dish here
import math
for _ in range(int(input())):
    n,a=map(int,input().split())
    temp=math.ceil(a/100)
    if temp>n:
        print(temp-n)
    else:
        print(0)
