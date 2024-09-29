# https://www.codechef.com/problems/STRONGTABLE?tab=statement
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    sm=sum(lst)
    lst.sort()
    m=0
    for i in range(n):
        m=max(m,lst[i]*(n-i))
    print(m)
