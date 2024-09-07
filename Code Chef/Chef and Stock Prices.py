# cook your dish here
for _ in range(int(input())):
    s,a,b,c=map(int,input().split())
    temp=s+((s*c))/100
    if temp>=a and temp<=b:
        print("Yes")
    else:
        print("No")
