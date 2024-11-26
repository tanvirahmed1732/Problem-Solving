# cook your dish here
for _ in range(int(input())):
    s,x,y,z=map(int,input().split())
    if s>=x+y+z:
        print(0)
    elif s>=min(x,y)+z:
        print(1)
    else:
        print(2)
