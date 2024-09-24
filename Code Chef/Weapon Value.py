# https://www.codechef.com/problems/SC31
for _ in range(int(input())):
    n=int(input())
    lst=['']*n
    ans=0
    for i in range(n):
        lst[i]=input()
    for i in range(10):
        temp=0
        for j in range(n):
            if lst[j][i]=='1':
                temp+=1
        if temp%2==1:
            ans+=1
    print(ans)
