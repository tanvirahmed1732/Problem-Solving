# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    n=y//x
    if z-n<=0:
        print(0)
    else:
        print(z-n)
      
