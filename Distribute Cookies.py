# Distribute Cookies
for _ in range(int(input())):
    n,m=map(int,input().split())
    if m<n:
        print(n-m)
    elif m%n < n/2:
        print(m%n)
    else:
        print(n-m%n)
