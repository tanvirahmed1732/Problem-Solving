# https://www.codechef.com/problems/CHRISCANDY
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    mx=0
    c=0
    for i in range(n):
        mx=max(mx,lst[i])
        if mx>lst[i]:
            c+=1
    print(c)
