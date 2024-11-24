# https://www.codechef.com/problems/FFL
import numpy as np
for _ in range(int(input())):
    n,s=map(int,input().split())
    pr=np.array(list(map(int,input().split())))
    lst=np.array(list(map(int,input().split())))
    if (lst==0).all() or (lst==1).all():
        print('no')
        continue
    df=np.min(pr[lst==0])
    fr=np.min(pr[lst==1])
    if s+df+fr>100:
        print("no")
    else:
        print('yes')
