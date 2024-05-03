# cook your dish here
for _ in range(int(input())):
    n,x,y = map(int,input().split())
    lst = list(map(int,input().split()))
    sm = 0
    for i in lst:
        if i*x<y:
            sm+=i*x
        else:
            sm+=y
    print(sm)
