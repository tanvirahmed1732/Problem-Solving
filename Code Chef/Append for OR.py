# https://www.codechef.com/problems/APPENDOR?tab=statement
for _ in range(int(input())):
    n,y=map(int,input().split())
    lst=list(map(int,input().split()))
    temp=0
    for i in lst:
        temp=temp|i
    t=temp^y
    if temp|t==y:
        print(t)
    else:
        print(-1)
