# cook your dish here
for _ in range(int(input())):
    n,x,k=map(int,input().split())
    print( 0 if k == 0 else k//x if n*x>k else n)
