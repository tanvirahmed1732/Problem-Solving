# https://www.codechef.com/problems/BESTBATS
import math
for _ in range(int(input())):
    lst=list(map(int,input().split()))
    k=int(input())
    lst.sort(reverse=True)
    ar=lst[:k]
    temp=ar[k-1]
    # print(lst.count(temp),ar.count(temp))
    # print(ar)
    print(math.comb(lst.count(temp),ar.count(temp)))
