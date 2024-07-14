# cook your dish here
import math
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    if n == 2:
        print(sum(lst))
    else:
        lst.sort()
        sm = lst[0] + lst[2]
        for i in range(2,n-1):
            sm+=(lst[i]+lst[i+1])
        sm+=(lst[n-1]+lst[1])
        print(sm)
