# Marathon
for _ in range(int(input())):
    D,d,a,b,c = map(int,input().split())
    t=0
    x=D*d
    if x>= 42:
        t=max(a,b,c)
    elif x>=21:
        t=max(a,b)
    elif x>=10:
        t=a
    print(t)
