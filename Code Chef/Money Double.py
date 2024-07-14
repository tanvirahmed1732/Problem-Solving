# cook your dish here
for _ in range(int(input())):
    x,y = map(int,input().split())
    if x>1000:
        for i in range(y):
            x = x * 2
    else:
        x+=1000
        for i in range(y-1):
            x=x*2
    print(x)
