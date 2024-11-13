# https://www.codechef.com/problems/VACCINE2
import numpy as np
for _ in range(int(input())):
    n,d=map(int,input().split())
    lst=list(map(int,input().split()))
    lst=np.array(lst)
    m=(lst>=80).sum()
    m+=(lst<=9).sum()
    ans=np.ceil(m/d)+np.ceil((n-m)/d)
    print(ans.astype(int))
