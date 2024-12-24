# cook your dish here
import math
for _ in range(int(input())):
    x,y,r=map(int, input().split())
    r=r//30
    x=x+r  
    print(math.ceil(x/y))
