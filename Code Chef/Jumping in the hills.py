# https://www.codechef.com/problems/HILLS
for _ in range(int(input())):
    n,u,d=map(int,input().split())
    lst=list(map(int,input().split()))
    ans=1
    check=True
    for i in range(n-1):
        if lst[i+1]==lst[i]:
            ans+=1
        elif lst[i+1]>lst[i] and lst[i+1]-lst[i]<=u:
            ans+=1
        elif lst[i+1]<lst[i] and lst[i]-lst[i+1]<=d:
            ans+=1
        elif lst[i+1]<lst[i] and check:
            ans+=1
            check=False
        else:
            break
    print(ans)
