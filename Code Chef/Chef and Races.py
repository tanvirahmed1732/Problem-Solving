# cook your dish here
for _ in range(int(input())):
    x,y,a,b=map(int,input().split())
    if x==a:
        if y==b:
            print(0)
        else:
            print(1)
    elif x==b:
        if y==a:
            print(0)
        else:
            print(1)
    else:
        if y==a or y==b:
            print(1)
        else:
            print(2)
