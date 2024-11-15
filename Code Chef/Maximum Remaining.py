# https://www.codechef.com/problems/MAXREM
import numpy as np
n=int(input())
lst=np.array(list(map(int,input().split())))
mx=np.max(lst)
if lst[lst!=mx].size==0:
    print(0)
else:
    print(np.max(lst[lst!=mx])%mx)
