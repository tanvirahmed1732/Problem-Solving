# https://www.codechef.com/problems/ADADISH?tab=statement
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    lst.sort(reverse = True)
    a,b=0,0
    for i in lst:
        if a<=b:
            a+=i
        else:
            b+=i
    print(max(a,b))
