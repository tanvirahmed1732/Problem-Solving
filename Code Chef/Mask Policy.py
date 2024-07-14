# Mask Policy
for _ in range(int(input())):
    n,a = map(int,input().split())
    if((n/2)>=a):
        print(a)
    else:
        print(n-a)
