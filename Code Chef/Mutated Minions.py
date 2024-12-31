# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    ans=0
    for i in lst:
        if (i+k)%7==0:
            ans+=1
    print(ans)
