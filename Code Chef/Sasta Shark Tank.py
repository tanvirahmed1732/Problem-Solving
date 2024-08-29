# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    a=(a*100)/10 
    b=(b*100)/20
    if a==b:
        print("ANY")
    elif a>b:
        print("FIRST")
    else:
        print("SECOND")
