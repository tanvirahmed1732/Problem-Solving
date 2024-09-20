# https://www.codechef.com/problems/AVG
for _ in range(int(input())):
    n,k,v=map(int,input().split())
    lst=list(map(int,input().split()))
    sm=sum(lst)
    m=n+k
    ml=m*v
    if sm>=ml:
        print(-1)
    else:
        sm=ml-sm
        if sm%k==0:
            print(sm//k)
        else:
            print(-1)
