# Fit in Data Type
for _ in range(int(input())):
    n,x = map(int, input().split())
    if x == 0:
        print(0)
    elif x<=n:
        print(x)
    else:
        print(x % (n+1))
