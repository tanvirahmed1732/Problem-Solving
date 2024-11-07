# https://www.codechef.com/problems/NEWPIECE
for _ in range(int(input())):
    a,b,p,q=map(int,input().split())
    x=(a+b)%2
    y=(p+q)%2
    if a==p and b==q:
        print(0)
    elif x==y:
        print(2)
    else:
        print(1)
