# Chocolate Distribution
for _ in range(int(input())):
    n = int(input())
    if n%2==1:
        t=(n-1)//2
        print(1,t,t)
    else:
        print(1,1,n-2)
