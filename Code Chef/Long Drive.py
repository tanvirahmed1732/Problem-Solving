# Long Drive
#10*70=600
for _ in range(int(input())):
    x,y=map(int,input().split())
    z=x*10
    t=10
    while(True):
        if z/t>=y:
            break 
        z+=100
        t+=1
    print(t-10)
