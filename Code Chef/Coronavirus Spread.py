# https://www.codechef.com/problems/COVID19
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    ar=[]
    k=1
    for i in range(n-1):
        if lst[i+1]-lst[i]>2:
            ar.append(k)
            k=1
        else:
            k+=1
    ar.append(k)
    print(min(ar),max(ar))
