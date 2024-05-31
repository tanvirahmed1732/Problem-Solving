# Even Sum Subarray
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    s = sum(lst)
    t = s
    tt=n
    for i in range(n):
        if s%2==0:
            print(tt)
            break
        elif t%2==0:
            print(tt)
            break
        else:
            s-=lst[i]
            t-=lst[n-i-1]
            tt-=1
    else:
        if lst[0]%2 == 0:
            print(1)
        else:
            print(0)
