# https://www.codechef.com/problems/MAKEPERM
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    for i in range(n):
        if lst[i]>i+1:
            print("NO")
            break
    else:
        print("YES")
