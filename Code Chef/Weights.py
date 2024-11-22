# cook your dish here
for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    if w==x or w==y or w==z:
        print("YES")
    elif w==x+y or w==x+z or w==y+z:
        print("YES")
    elif w== x+y+z:
        print("YES")
    else:
        print("NO")
