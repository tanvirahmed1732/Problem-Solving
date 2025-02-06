# https://www.codechef.com/problems/DOUBLEDDIST?tab=statement
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    f=False
    for i in range(1,n-1):
        if (lst[i]-lst[i-1] != 2*(lst[i+1]-lst[i])) and (2*(lst[i]-lst[i-1]) != lst[i+1]-lst[i]):
            f=True
            break
    if f:
        print("NO")
    else:
        print("YES")
