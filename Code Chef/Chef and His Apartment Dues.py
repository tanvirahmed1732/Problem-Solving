# https://www.codechef.com/problems/CHEFAPAR
for _ in range(int(input())):
    n=int(input())
    z=0
    lst=list(map(int,input().split()))
    t=lst[0]
    if t==0:
        c=0
    else:
        c=n
    for i in range(n):
        if t==1:
            if lst[i]==0:
                c=i
                t=0
        if lst[i]==0:
            z+=1
    print((z*1000) + (n-c)*100)
