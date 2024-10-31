# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x%3==0:
        print((x*y)+((x//3)-1)*z)
    else:
        print((x*y)+(x//3)*z)
