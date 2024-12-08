# cook your dish here
for _ in range(int(input())):
    a,x,b,y=map(int,input().split())
    a=a/x 
    b=b/y
    if a==b:
        print("Equal")
    elif a>b:
        print("Alice")
    else:
        print("Bob")
