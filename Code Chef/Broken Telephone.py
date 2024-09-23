# https://www.codechef.com/problems/BROKPHON
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    temp=lst[0]
    ans=0
    im=False
    for i in range(1,n):
        if temp!=lst[i] and im == False:
            ans+=2
            temp=lst[i]
            im=True
        elif temp!=lst[i]:
            ans+=1
            temp=lst[i]
        else:
            im=False
    print(ans)
