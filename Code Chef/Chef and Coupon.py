# https://www.codechef.com/problems/COUPON2
import numpy as np
for _ in range(int(input())):
    d,c=map(int,input().split())
    a=np.array(list(map(int,input().split())))
    b=np.array(list(map(int,input().split())))
    cop=(np.sum(a) if np.sum(a)>=150 else np.sum(a)+d)+(np.sum(b) if np.sum(b)>=150 else np.sum(b)+d)+c
    wcop=np.sum(a)+np.sum(b)+2*d
    if (cop<wcop):
        print("YES")
    else:
        print("NO")
