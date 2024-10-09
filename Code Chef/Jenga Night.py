# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    if n>x:
        print("NO")
    elif x%n==0:
        print("YES")
    else:
        print ("NO")
