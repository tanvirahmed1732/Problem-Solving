# https://www.codechef.com/problems/WEPCH
import math
for _ in range(int(input())):
    h,x,y,z,k=map(int,input().split())
    if y*k>=h:
        temp=math.ceil(h/y)
    else:
        t=y*k
        t=h-t
        temp=math.ceil(t/z)+k
    print(min(math.ceil(h/x),temp))
