# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    if 2*x<y:
        xx=500-x*2
        yy=1000-(y+x)*4
    else:
        yy=500-y*4
        xx=1000-(y+x)*2
    print(xx+yy)
