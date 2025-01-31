# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DPOLY
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    ans=0
    for i in range(n-1,-1,-1):
        if lst[i]!=0:
            ans=i
            break
    print(i)
