# cook your dish here
import math
for _ in range(int(input())):
    h,x,y=map(int,input().split())
    h-=y  
    if h<=0:
        print(1)
    else:
        print(math.ceil(h/x)+1)
