# cook your dish here
import math
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    print(math.ceil(a/(b*c)))
