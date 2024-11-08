# https://www.codechef.com/problems/TWODIFFPALIN
for _ in range(int(input())):
    a,b=map(int,input().split())
    m=a%2
    n=b%2
    if m==0 and n==0:
        print("Yes")
    elif m==1 and n==1:
        print("No")
    elif a==1 or b==1:
        print("No")
    else:
        print("Yes")
