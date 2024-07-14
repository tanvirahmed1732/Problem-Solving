# Am I Lucky!
for _ in range(int(input())):
    n,x,k=map(int,input().split())
    y=n-x
    x=x%k 
    y=y%k
    print(abs(x-y))
