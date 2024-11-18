# https://www.codechef.com/problems/CHFPARTY
import numpy as np 
for _ in range(int(input())):
    n=int(input())
    lst=np.array(list(map(int,input().split())))
    lst.sort()
    i=0
    for j in lst:
        if j<=i:
            i+=1
    print(i)
