# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    if n-x>n/2:
        print(x)
    else:
        print(n-x)
