# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    if k == 0:
        print(n)
    else:
        print(n%k)
