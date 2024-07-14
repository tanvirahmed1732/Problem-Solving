# Non-Negative Product
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int, input().split()))
    t=0
    for i in lst:
        if i == 0:
            print(0)
            break
        elif i<0:
            t+=1
    else:
        if t%2==0:
            print(0)
        else:
            print(1)
