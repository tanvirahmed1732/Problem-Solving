# World Chess Championship
for _ in range(int(input())):
    x=int(input())
    s=input()
    c=s.count('C')
    n=s.count('N')
    if n==c:
        print(55*x)
    elif c>n:
        print(60*x)
    else:
        print(40*x)
