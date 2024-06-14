#Chef and Fruits
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    a=abs(n-m)-k
    print(0 if a<=0 else a)
