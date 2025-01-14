# https://www.codechef.com/problems/S02E10
for _ in range(int(input())):
    n,x,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    count=0
    for i in range(n):
        if abs(a[i]-b[i])<=k: #if the condition match, count
            count+=1
    if count>=x: #if required number of matching found
        print("YES")
    else:
        print("NO")
