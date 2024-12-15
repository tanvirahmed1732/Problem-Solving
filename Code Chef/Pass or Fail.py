# cook your dish here
for _ in range(int(input())):
    n,x,p=map(int,input().split())
    m=x*3-(n-x)
    if m>=p:
        print("PASS")
    else:
        print("FAIL")
