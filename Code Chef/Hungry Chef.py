# Hungry Chef
for _ in range(int(input())):
    x,y,n,r = map(int, input().split())
    if (n*x)>r:
        print(-1)
    else:
        p = min(n,(r - (n*x))//(y-x))
        print(n-p,p)
