# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    m=max(a+c,a+d)
    m=max(m,b+c,b+d)
    print(m)
