# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    ans=0
    for i in lst:
        if i>=10 and i<=60:
            ans+=1
    print(ans)
