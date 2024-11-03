# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    m=x//y
    print(m+x-(m*y))
