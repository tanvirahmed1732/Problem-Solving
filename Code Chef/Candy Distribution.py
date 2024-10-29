# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    print("Yes" if (n/m)%2==0 else "No")
