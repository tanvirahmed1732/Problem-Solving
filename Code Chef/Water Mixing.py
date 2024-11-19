# cook your dish here
for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    if a>=b:
        if y>=(a-b):
            print("YES")
        else:
            print("NO")
    else:
        if x>=(b-a):
            print("YES")
        else:
            print("NO")
